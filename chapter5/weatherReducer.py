import sys
import logging

from util import reducer_logfile
logging.basicConfig(filename=reducer_logfile, format='%(message)s',
                    level=logging.INFO, filemode='w')

def reducer():
    '''
    Given the output of the mapper for this assignment, the reducer should
    print one row per weather type, along with the average value of
    ENTRIESn_hourly for that weather type, separated by a tab. You can assume
    that the input to the reducer will be sorted by weather type, such that all
    entries corresponding to a given weather type will be grouped together.

    In order to compute the average value of ENTRIESn_hourly, you'll need to
    keep track of both the total riders per weather type and the number of
    hours with that weather type. That's why we've initialized the variable 
    riders and num_hours below. Feel free to use a different data structure in 
    your solution, though.

    An example output row might look like this:
    'fog-norain\t1105.32467557'

    Since you are printing the output of your program, printing a debug 
    statement will interfere with the operation of the grader. Instead, 
    use the logging module, which we've configured to log to a file printed 
    when you click "Test Run". For example:
    logging.info("My debugging message")
    Note that, unlike print, logging.info will take only a single argument.
    So logging.info("my message") will work, but logging.info("my","message") will not.
    '''

    # Accumulator
    riderCounts = {}
    
    for line in sys.stdin:
        # Convert input to record
        data = line.strip().split('\t')
        
        # Skip any non-k-v pairs
        if len(data) != 2:
            continue
        
        # Process record
        k, v = (data[0],data[1])
        if k in riderCounts:
            entries, count = riderCounts[k]
            riderCounts[k] = (entries+float(v), count+1)
        else:
            riderCounts[k] = (float(v), 1)
        
    # Format and emit results
    for k, v in riderCounts.items():
        entries, count = v
        print(k + '\t' + str(entries/count))

reducer()

