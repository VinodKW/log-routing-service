import json
import fcntl
import os
from celery import shared_task
from .modules import process_logs_from_shard, get_next_shard_index, get_shard_filename, NUM_SHARDS

@shared_task
def create_log(data):
    shard_index = get_next_shard_index()
    filename = get_shard_filename(shard_index)
    with open(filename, 'a') as file:
        try:
            print("Create log operations started.")

            # Acquire an exclusive lock before writing to the file
            fcntl.flock(file, fcntl.LOCK_EX)
            
            # Write the JSON data to the file
            file.write(json.dumps(data))
            file.write('\n')

            print("Create log operations completed.")
        finally:
            # Release the lock
            fcntl.flock(file, fcntl.LOCK_UN)


@shared_task
def process_logs_from_queue():
    print("Process log operation started.")
    for shard_index in range(NUM_SHARDS):
        filename = get_shard_filename(shard_index)
        if os.path.exists(filename):
            process_logs_from_shard(filename)
        else:
            print("No data to process.")
    print("Process log operation completed.")
