# In decorators.py

import functools
import time

# Timer Function
# It will measure the time a function takes to execute and print the duration to the console


def timer(func):

	'''Print the runtime of the decorated function'''
	@functools.wraps(func)

	def wrapper_timer(*args, **kwargs):
		start_time = time.perf_counter()#stores the time before function starts running
		value = func(*args, **kwargs)
		end_time = time.perf_counter()#stores the time just after the function finishes
		run_time = end_time - start_time

		print(f"Finished {func.__name__!r} in {run_time:4f} secs.")
		return value

	return wrapper_timer





#Debugging Function
#It will print the arguments the function is called with as well as its return value every time thr fuction is called


def deubg(func):

	'''Print the function signature and return value'''
	@functools.wraps(func)

	def wrapper_debug(*args, **kwargs):
		args_repr = [repr(a) for a in args]#create a list of positional arguments
		kwargs_repr = [f"{k}={v!r}" for k,v in kwargs.items()]#create a list of keywaord arguments
		signature = ", ".join(args_repr + kwargs_repr)
		print(f"Calling {func.__name__}({signature})")
		value = func(*args, **kwargs)
		print(f"{func.__name__!r} returned : {value!r}")
		return value

	return wrapper_debug
