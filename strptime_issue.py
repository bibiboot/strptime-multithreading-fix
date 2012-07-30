import datetime
import thread
import sys

"""
Pass either 'Replicate' or 'Fix' as the 
parameter while running the file.
"""

def print_time( threadName, delay):
   # Implementaion code of strptime
   count = 0
   while count < 5:
      count += 1
      try:
          print threadName, datetime.datetime.strptime('20120301', '%Y%m%d')
      except Exception, e:
          print 'Exception: ',  threadName, str(e)

def run(status):
    """
    Creates the two thread for 
    calling the code using the 
    strptime.
    """
    try:
        if status == 'Fix':
            # Calling the strptime before the creation of the threads
            print datetime.datetime.strptime('20120301', '%Y%m%d')
        thread.start_new_thread( print_time, ("Thread-1", 2, ) )
        thread.start_new_thread( print_time, ("Thread-2", 4, ) )
    except:
        print "Error: unable to start thread"

    while 1:
        pass

if __name__ == '__main__':
    status = sys.argv[1]
    if status not in [ 'Replicate', 'Fix' ]:
        print 'Error: First argument must be either Replicate or Fix'
        sys.exit()
    run(status)
