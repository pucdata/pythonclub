"""
demo of running a slow function on multiple processors
"""

def my_slow_function(x):
	import time
	print 'slow computing of %d ...' % x
	time.sleep(1)
	return x**2

import joblib

tasks = (joblib.delayed(my_slow_function)(x) for x in range(30))
# so far nothing has been executed

# now we run it in parallel, using all processors
results = joblib.Parallel(n_jobs=-1)(tasks)

print results

