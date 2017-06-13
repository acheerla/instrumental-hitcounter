import collections
import bisect
import time
import numpy as np

class Client(object):
	def __init__(self):
		self.hits = []
		self.start = time.time()


	def request_count(self, start_time):
		''' Counts the number of hits in the period of time starting "start_time" seconds ago and ending at the current time.
		#Arguments
			start_time: length of requested time period

		#Returns
			number of hits
		'''

		ind = bisect.bisect_right(self.hits, time.time()- self.start - start_time)
		return len(self.hits) - ind;

	def register_hit(self):
		''' Registers a hit at the current time'''
		self.hits.append(time.time() - self.start )
