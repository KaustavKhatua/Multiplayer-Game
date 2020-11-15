import _thread
import time

a = 1

def print_function():
    global a
    print(a)
    a = a + 4

# print_function()
# _thread.start_new_thread(print_function, (1,))
# _thread.start_new_thread(print_function, (1, ))
_thread.start_new_thread(print_function, ( ))
time.sleep(5)

print(a)