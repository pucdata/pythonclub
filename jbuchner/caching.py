"""
demo of caching a slow function
"""

def my_slow_function(x):
	import time
	print 'slow computing of %d ...' % x
	time.sleep(1)
	return x**2

import joblib
mem = joblib.Memory('.', verbose=False)

my_slow_function = mem.cache(my_slow_function)

# or do this:
@mem.cache
def my_slow_function(x):
	import time
	print 'slow computing of %d ...' % x
	time.sleep(1)
	return x**2


# use it
print 'starting...'
for x in range(10):
	y = my_slow_function(x)
	print 'result:', y
print 'done!'
	
# when you run this script a second time, it will use the cache
