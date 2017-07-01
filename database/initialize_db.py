#!/usr/bin/env python
import os
import sys

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(CURRENT_DIR))

import json
import boto3
import decimal
import logging
from botocore.exceptions import ClientError


# Helper class to convert a DynamoDB item to JSON.
class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            if o % 1 > 0:
                return float(o)
            else:
                return int(o)
        return super(DecimalEncoder, self).default(o)


class DynamoDB(object):
    """docstring for DynamoDB"""

    def __init__(self, table_name, DEPLOY=False):
        super(DynamoDB, self).__init__()
        self.table_name = table_name
        self.DEPLOY = DEPLOY

        # this is to make the difference when working in local or server
        if DEPLOY:
            self.dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
        else:
            self.dynamodb = boto3.resource('dynamodb', region_name='us-east-1', endpoint_url="http://localhost:8000")

        # this is any easy way to handle the exception, checking if the table is created or not
        try:
            self.create_table();
            pass
        except:
            pass
        pass

    # since there will be only one table so hardcoded.
    def create_table(self):
        table = self.dynamodb.create_table(
            TableName=self.table_name,
            KeySchema=[
                {
                    'AttributeName': 'classification',
                    'KeyType': 'HASH'  # Partition key
                },
                {
                    'AttributeName': 'start_time',
                    'KeyType': 'RANGE'  # Sort Key
                }
            ],
            AttributeDefinitions=[
                {
                    'AttributeName': 'classification',
                    'AttributeType': 'S'
                },
                {
                    'AttributeName': 'start_time',
                    'AttributeType': 'N'
                }
            ],
            ProvisionedThroughput={
                'ReadCapacityUnits': 10,
                'WriteCapacityUnits': 10
            }
        )
        if self.DEPLOY == False:
            print("Table status:", table.table_status)

        pass

    # batchwrite to the dynamodb
    def batch_write(self, items):
        table = self.dynamodb.Table(self.table_name)

        with table.batch_writer(overwrite_by_pkeys=['classification', 'start_time']) as batch:
            logging.info("batch writer working")
            for item in items:
                batch.put_item(Item=item)

    pass

    # put_data inputs a dictionary file which must have but the keys
    def put_data(self, items):

        table = self.dynamodb.Table(self.table_name)
        for i in items:
            response = table.put_item(Item=i)

            if self.DEPLOY == False:
                print("Put item succeeded")
                print(json.dumps(response, indent=4, cls=DecimalEncoder))
        pass

    # get_data inputs a dictionary file which must have a dictionary of queries.
    def get_data(self, key):
        table = self.dynamodb.Table(self.table_name)
        try:
            response = table.get_item(Key=key)
            pass
        except ClientError as e:
            print(e.response['Error']['Message'])
        else:
            item = response['Item']

            if self.DEPLOY == False:
                print("GetItem succeeded:")
                print(json.dumps(item, indent=4, cls=DecimalEncoder))
            pass
        pass

    # This is to scan the data and get return the value in JSON
    def scan_data(self, fe):
        table = self.dynamodb.Table(self.table_name)
        response = table.scan(FilterExpression=fe)

        if self.DEPLOY == False:
            for i in response['Items']:
                print(json.dumps(i, cls=DecimalEncoder))

        # print (response)

        while 'LastEvaluatedKey' in response:
            response = table.scan(FilterExpression=fe)

            if self.DEPLOY == False:
                for i in response['Items']:
                    print(json.dumps(i, cls=DecimalEncoder))
                    pass
                pass
            pass

        return response

    # True : Ascending, False : Descending
    def query_data(self, Ke, Fe, sort=True):
        table = self.dynamodb.Table(self.table_name)

        if Fe == None:
            response = table.query(
                KeyConditionExpression=Ke,
                ScanIndexForward=sort
            )
        else:
            response = table.query(
                KeyConditionExpression=Ke,
                ScanIndexForward=sort,
                FilterExpression=Fe
            )

        if self.DEPLOY == False:
            for i in response['Items']:
                print(i)

        return json.dumps(response['Items'], cls=DecimalEncoder)
