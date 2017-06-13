from client_api import Client
import time


def test1(): #consecutive, instantaneous hits
	c = Client()
	assert c.request_count(1) == 0, "ERROR: No hits should result in a count of 0"

	c.register_hit()
	assert c.request_count(1) == 1, "ERROR: One hit should should result in a count of 1"

	c.register_hit()
	c.register_hit()
	c.register_hit()
	assert c.request_count(2) == 4, "ERROR: 4 hits should should result in a count of 4"


def test2(): #hit followed by a period of time
	c = Client() 
	c.register_hit()
	time.sleep(2.5)
	assert c.request_count(1) == 0, "ERROR: One hit 2.5 s ago. Count from 1 s ago should return 0"
	assert c.request_count(3) == 1, "ERROR: One hit 2.5 s ago. Count from 3 s ago should return 0"


def test3(): #hits over time
	c = Client()
	c.register_hit()
	time.sleep(2)
	c.register_hit()
	assert c.request_count(1) == 1, "ERROR: One hit 0 s ago, one hit 2 s ago. Count from 1 s ago should return 1"
	assert c.request_count(3) == 2, "ERROR: One hit 0 s ago, one hit 2 s ago. Count from 3 s ago should return 2"


def test4(): #edge case
	c = Client()
	c.register_hit()
	time.sleep(1.99) 
	assert c.request_count(2) == 1, "ERROR: One hit 1.99 s ago. Count from 2 ms ago should return 1" #cannot be exactly 1.99 due to lag


if __name__ == "__main__":
	test1()
	print "Test 1 - testing consecutive, instantaneous hits - was successful"
	test2()
	print "Test 2 - testing a request's sensitivity to time - was successful"
	test3()
	print "Test 3 - testing hits separated by time - was successful"
	test4()
	print "Test 4 - testing boundary cases - was successful"