"""
Explain about Closures
"""

# e.g 1
def outer_func(msg):
    message = msg
    def inner_func():
        print(message)
    # if return function without (), means return function but not excute it.
    return inner_func

# these two variable just stored "Hi" and "Hello", but not excute them.
hi_func = outer_func('Hi') # now hi_func = inner_func with a message "Hi".
hello_func = outer_func ('Hello') # now hello_func = inner_func with a message "Hello".

# output 'Hi'
hi_func() #now excute hi_func, same as excute inner_func with message "Hi".

# output 'Hello'
hello_func()




# e.g. 2

import logging
logging.basicConfig(filename="example.log", level=logging.INFO)

def logger(func):
    # *args means take any number as arguments.
    def log_func(*args):
        logging.info('Running "{}" with arguments {}'.format(func.__name__, args))
        print(func(*args))
    return log_func

def add(x, y):
    return x+y

def sub(x, y):
    return x-y

add_logger = logger(add)
sub_logger = logger(sub)

add_logger(3, 3) # output 6
add_logger(4, 5) # output 9

sub_logger(10, 5) # output 5
sub_logger(20, 10) # output 10
