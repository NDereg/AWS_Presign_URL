# -*- coding: utf-8 -*-
""" AWS_Presign_URL for S3 Object

"""

import os
import json
import logging
import boto3


def main(event):
    """Main Worker"""
    enable_logging()
    config = import_config()
    obj_pointer = parse_event_data(event)
    obj = get_s3_object(obj_pointer)
    url = presign_s3_url(obj_pointer, config)
    create_email_msg(obj.bucket_name, obj.key, url, config)


def enable_logging():
    """Enables Logging for Console and CloudWatch"""
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)


def import_config():
    """Import ./data/config.json"""
    with open(os.path.abspath('./data/config.json')) as json_config:
        config_template = json.load(json_config)
        config_default = config_template.get('default')
    return config_default


def parse_event_data(event):
    """Parses Event Data for S3 Object"""
    s3_records = event.get('Records')[0].get('s3')
    bucket = s3_records.get('bucket').get('name')
    key = s3_records.get('object').get('key')
    data = {"Bucket": bucket, "Key": key}
    return data


def get_s3_object(obj_pointer):
    """Gets S3 Object"""
    s3 = boto3.resource('s3')
    bucket = obj_pointer.get('Bucket')
    filename = obj_pointer.get('Key')
    obj = s3.Object(bucket, filename)
    return obj


def presign_s3_url(obj_pointer, conf):
    """Presign URL for S3 Object"""
    s3 = boto3.client('s3')
    url = s3.generate_presigned_url(
        ClientMethod='get_object',
        Params=obj_pointer,
        ExpiresIn=conf.get('expire'))
    return url


def create_email_msg(bucket, file, url, conf):
    """Create Email Message"""
    email_msg = 'Bucket Name: {}\nFile Name: {}\nURL: {}'.format(
        bucket, file, url)
    send_email(conf.get('from'), conf.get(
        'to'), conf.get('subj'), email_msg)


def send_email(src, dest, subj, msg):
    """Send email using AWS SES"""
    ses = boto3.client('ses')
    ses.send_email(
        Source=src,
        Destination={
            'ToAddresses': dest
        },
        Message={
            'Subject': {
                'Data': subj
            },
            'Body': {
                'Text': {
                    'Data': msg
                }
            }
        }
    )



