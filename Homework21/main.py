import os
import threading
from json_interpreter import parse_json
import queue
from queue_processor import process_queue

folder_path = './data/'

json_files = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith('.json')]

threads = []
for file in json_files:
    thread = threading.Thread(target=parse_json, args=(file,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("------------------------------DAVALEBA 2-----------------------------")
number_queue = queue.Queue()

streams = ["Stream-1", "Stream-2", "Stream-3"]

threads = []
for stream in streams:
    thread = threading.Thread(target=process_queue, args=(number_queue, stream))
    threads.append(thread)
    thread.start()

numbers = [10, 25, 33, 42, 56, 77, 88, 91, 100]
for num in numbers:
    number_queue.put(num)

for thread in threads:
    thread.join()

sorted_numbers = sorted(numbers)
print("Dalagebuli ricxvebi:", sorted_numbers)
print("Yvela Davaleba Shesrulebulia.")