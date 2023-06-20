import asyncio
import aiohttp

url = 'http://django-server:8000/api/log'
headers = {'Content-Type': 'application/json'}

payload = {
    "unix_ts": 1684129671,
    "user_id": 123456,
    "event_name": "login"
}

successful_requests = 0


async def send_request(session, payload):
    global successful_requests

    max_retries = 3
    retry_count = 0

    while retry_count < max_retries:
        try:
            async with session.post(url, headers=headers, json=payload) as response:
                if response.status == 201:
                    successful_requests += 1
                else:
                    print("Request failed with status code:", response.status)
            break  # Break out of the retry loop if request is successful
        except (aiohttp.ClientError, aiohttp.ClientConnectionError) as e:
            retry_count += 1
            # Wait for a short delay before retrying
            await asyncio.sleep(1)


async def send_requests_concurrently():
    async with aiohttp.ClientSession() as session:
        tasks = []
        while True:
            # Create a batch of requests
            for _ in range(1000):
                task = send_request(session, payload)
                tasks.append(task)

            # Send the batch of requests concurrently
            await asyncio.gather(*tasks)

            # Clear the tasks list
            tasks.clear()

            # Print the number of successful requests
            print("Total successful requests:", successful_requests)

# Run the event loop
loop = asyncio.get_event_loop()
loop.run_until_complete(send_requests_concurrently())
