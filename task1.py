import collections
import random
import time


def generate_request():
    request_id = random.randint(1, 100)
    print(f"Pushing a new order     # {request_id}")
    queue.append(request_id)


def process_request():
    if queue:
        request_id = queue.popleft()
        print(f"Processing the order    # {request_id}")
    else:
        print("Queue is empty!")


try:
    queue = collections.deque()
    while True:
        generate_request()
        process_request()
        time.sleep(0.1)
except KeyboardInterrupt:
    print("Bye-bye")
