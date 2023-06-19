import os, fcntl, json
from .models import Log

NUM_SHARDS = 10
CURRENT_SHARD_INDEX = 0
SHARDS_DIRECTORY = 'shards'


def get_next_shard_index():
    global CURRENT_SHARD_INDEX
    shard_index = CURRENT_SHARD_INDEX
    CURRENT_SHARD_INDEX = (CURRENT_SHARD_INDEX + 1) % NUM_SHARDS
    return shard_index


def get_shard_filename(shard_index):
    filename = f'data_queue_{shard_index}.json'
    return os.path.join(SHARDS_DIRECTORY, filename)


def process_logs_from_shard(filename):
    with open(filename, 'r+') as file:
        try:
            # Acquire an exclusive lock before reading or writing
            fcntl.flock(file, fcntl.LOCK_EX)
            
            # Read the contents of the file as a string
            file_contents = file.read()
            
            # Split the string into individual JSON objects
            objects = file_contents.strip().split('\n')

            # List to store the Log objects
            log_objects = []
            
            ## Process each JSON object individually
            for obj_str in objects:
                if obj_str:
                    obj = json.loads(obj_str)
                    
                    # Create a Log object and add it to the list
                    log_objects.append(Log(**obj))
            
            # Bulk create the Log objects
            Log.objects.bulk_create(log_objects)
            
            # Truncate the file to remove the processed data
            file.seek(0)
            file.truncate()
            
             # Write the remaining data back to the file (which is empty in this case)
            file.write('')
            
            # Flush the changes to the file
            file.flush()
        finally:
            # Release the lock
            fcntl.flock(file, fcntl.LOCK_UN)