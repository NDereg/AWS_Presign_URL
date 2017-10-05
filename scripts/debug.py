# -*- coding: utf-8 -*-
"""
Return from Lambda
"""

import os
import logging

# Sample return from Lambda, update 'test-bucket' and 'NewText.zip'
EVENT = {
    'Records': [{
        'eventVersion': '2.0',
        'eventSource': 'aws:s3',
        'awsRegion': 'us-east-1',
        'eventTime': '2017-06-19T18:25:08.048Z',
        'eventName': 'ObjectCreated:Put',
        'userIdentity': {'principalId': 'AWS:ABCDEFGHIJKLMNOP'},
        'requestParameters': {'sourceIPAddress': '11.11.11.11'},
        'responseElements': {
            'x-amz-request-id': '00AB00AB00AB00AB',
            'x-amz-id-2': 'dK387SkSAD90802akDLKAlka9020s87gfwaKaad8907s=3'
        },
        's3': {
            's3SchemaVersion': '1.0',
            'configurationId': '60ff49s-54d3-78adf-912f-765234v96a',
            'bucket': {
                'name': 'test-bucket',
                'ownerIdentity': {'principalId': 'KH4HGL18941L'},
                'arn': 'arn:aws:s3:::test-bucket'
            },
            'object': {
                'key': 'NewText.zip',
                'size': 0,
                'eTag': 'd41d8cd98f00b204e9800998ecf8427e',
                'sequencer': '0059481703F24B8E4F'
            }
        }
    }]
}


def enable_info_logging():
    """Enable Info Level Logging Messages"""
    logging_conf = {
        'level': logging.INFO,
        'format': '%(asctime)s %(levelname)s %(message)s',
        "datefmt": '%H:%M:%S'
    }
    logging.basicConfig(**logging_conf)


if __name__ == '__main__':
    enable_info_logging()
    # ensures the cwd is root of project
    __WS_DIR__ = os.path.dirname(os.path.realpath(__file__))
    os.chdir('{}/..'.format(__WS_DIR__))

    # execute lambda_handler
    from handler import lambda_handler
    lambda_handler(EVENT, None)
