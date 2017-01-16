# coding=utf-8

# Push test data to Splunk script

# For this to work, you need to do the following:
# 1. Use Pip to install the splunklib client
# 2. Create an index called performance
# 3. Change the password below

import splunklib.client as client
import time
from time import gmtime, strftime
from random import randint
import random

host = 'localhost'
sourcetype = 'test_availability_data'
port = 8089
index = 'performance'
username = 'admin'
password = 'CHANGEME'
increment = 5


def splunk_connect():
    print 'Initiating contact with Splunk'

    try:
        service=client.connect(
                           host=host,
                           port=port,
                           username=username,
                           password=password)
        print 'Connecting to Splunk, please wait'
        return service
    except Exception as error:
        print error

def splunk_push(index, sourcetype, startTime):
    service = splunk_connect()
    myindex = service.indexes['performance']
    mysocket = myindex.attach(sourcetype=sourcetype,host=host)

    current_time = str(strftime("%H:%M:%S"))
    sleep_time = time.sleep(randint(1,10))
    after_time = str(strftime("%H:%M:%S"))

    try:
        to_send =   "date_and_time=" + str(time.strftime('%c')) +\
                    " request_time=" + str(current_time) +\
                    " response_time=" + (after_time) +\
                    " uptime=" + str(int(time.time() - startTime) / 60) +\
                    " forcast_expected=" + str(int(time.time() - startTime) / 60) +\
                    " availability=" + str(randint(80, 100)) +\
                    " query_id=" + str("qn" + str(randint(1,250)) + "g0") +\
                    " query_type=" + str(random.choice(["bulk", "single"])) +\
                    " number_of_queries=" + str(randint(1,25)) +\
                    " single_match_time=" + str(randint(1,10)) +\
                    " bulk_match_time=" + str(randint(5,60)) +\
                    " data_returned=" + str(random.uniform(0,50)) +\
                    " percentage_failed_queries=" + str(randint(1,5)) +\
                    " component_name=" + str(random.choice(["HMRC","Crown Com", "Welsh Assembly", "Company House"])) +\
                    " success_flag=" + str(random.choice(["Success","Fail"])) +\
                    " time_to_ingest=" + str(randint(5,50000) / 60 / 60) +\
                    " spark_status=" + str(randint(1,3)) +\
                    " elastic_search_status=" + str(randint(1,3)) +\
                    " hdfs_status=" + str(randint(1,3)) +\
                    " flume_status=" + str(randint(1,3))
        mysocket.send(to_send)
        print to_send
        print 'Data push to Splunk is complete'
    except Exception as error :
        print error

if __name__ == '__main__':
    startTime = time.time()
    y = 0
    while True:
        splunk_push(index, sourcetype, startTime)
        y += 1
        print "Number of pushes: ", y
        time.sleep(increment)
