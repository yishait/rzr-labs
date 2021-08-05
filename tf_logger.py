#!/usr/bin/env python3

import sys
import logging
import io
import time
import boto3
log_name = sys.argv[1]

start_time = time.time()
# logging.basicConfig(filename='logs.log', format='%(asctime)s %(levelname)s %(name)s: %(message)s', datefmt='%d-%b-%y %H:%M:%S', level=logging.INFO)
logger = logging.getLogger("tfprocess")
logging.info("Program started ....")
logger.setLevel(logging.INFO)
log_stringio = io.StringIO()
handler = logging.StreamHandler(log_stringio)
logger.addHandler(handler)
s3 = boto3.resource('s3')
s3_client = boto3.client('s3')
s3_client.upload_file(log_name, 'yishaitamir-logging', log_name)

s3.Object('yishaitamir-logging', log_name).upload_file(log_name)
s3.Bucket('yishaitamir-logging').upload_file(Filename=log_name,  Key='logs/')

print("Process Finsihed --- %s seconds ---" %(time.time() - start_time))