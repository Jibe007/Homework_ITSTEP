import threading

def process_queue(queue, stream_name):
    while not queue.empty():
        value = queue.get()
        is_even = "even" if value % 2 == 0 else "odd"
        print(f"Stream: {stream_name}, Value: {value}, Even: {is_even}")
        queue.task_done()
