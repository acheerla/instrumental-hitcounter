# Hit Counter
A small API where users can register hits and obtain the number of hits that occured in a specified time-period.  

## Code demonstration
The two actions a user can perform are written in the <b>Client</b> class.  
To register a hit:
```
c = Client()
c.register_hit()
```
To request a count starting from <i>t</i> seconds ago:   
```
c.request_count(t) 
```

## Testing . 
4 cases are tested in <b>test_suite.py</b>. If all cases are successful, the following should be printed out:  
```
Test 1 - testing consecutive, instantaneous hits - was successful
Test 2 - testing a request's sensitivity to time - was successful
Test 3 - testing hits separated by time - was successful
Test 4 - testing boundary cases - was successful
```
Otherwise, the appropriate error is printed; for instance:  
```
ERROR: One hit 0s ago, one hit 2 s ago. Count from 3s ago should return 2.
```
