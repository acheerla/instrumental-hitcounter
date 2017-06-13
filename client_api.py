import collections
import bisect
import time
import numpy as np

class Client(object):
	def __init__(self):
		self.hits = []
		self.start = time.time()


	def request_count(self, start_time):
		ind = bisect.bisect_right(self.hits, time.time()- self.start - start_time)
		return len(self.hits) - ind;

	def register_hit(self):
		self.hits.append(time.time() - self.start )
