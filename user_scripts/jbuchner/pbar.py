"""
demo of a progress bar
"""

import progressbar # install with $ pip install progressbar --user
pbar = progressbar.ProgressBar(widgets=[progressbar.Percentage(), 
	progressbar.Counter('%5d'), progressbar.Bar(), progressbar.ETA()])

sequence = range(1000)

for obj in pbar(sequence):
	# do some slow computation
	x = obj**2
	import time
	time.sleep(0.03)
	

