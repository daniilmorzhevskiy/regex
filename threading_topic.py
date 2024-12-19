'''import datetime

def test_do_something():
    print("I'm waiting to complete the task")
    datetime.sleep(5)
    print("I'm done")

for i in range(10):

 test_do_something()

print("Hello")
'''

import threading

def print_numbers():
    for i in range(5):
        print(i)


# Create a thread to run the print_numbers function
thread = threading.Thread(target=print_numbers)
thread.start()

# Continue executing the main program while the thread runs concurrently
print("Thread started!")