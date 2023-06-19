import requests
import json
from concurrent.futures import ThreadPoolExecutor

url = 'http://localhost:8000/api/log'
headers = {'Content-Type': 'application/json'}

payload = {
    "unix_ts": 1684129671,
    "user_id": 123456,
    "event_name": "login"
}

successful_requests = 0  # Counter for successful requests

def send_request(payload):
    global successful_requests  # Use the global keyword
    try:
        response = requests.post(url, headers=headers, data=json.dumps(payload))
        if response.status_code == 201:
            print("Request sent successfully")
            successful_requests += 1
        else:
            print("Request failed with status code:", response.status_code)
    except (requests.ConnectionError, requests.ConnectionResetError) as e:
        print("Request failed due to connection error:", str(e))

# Set the maximum number of concurrent threads
max_threads = 100

# Create a thread pool executor with the specified maximum number of threads
executor = ThreadPoolExecutor(max_workers=max_threads)

# Submit the requests to the executor
for _ in range(1000):
    executor.submit(send_request, payload)

# Shut down the executor to allow for clean exit
executor.shutdown()

# Print the number of successful requests
print("Total successful requests:", successful_requests)
