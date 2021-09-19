import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('sample_table')

def lambda_handler(event, context):
    response = table.get_item(Key={
        'record_id':'0'
    })
    record_count = response['Item']['record_count']
    record_count = record_count + 1
    print(record_count)
    
    response = table.put_item(Item={
        'record_id':'0',
        'record_count': record_count
    })
    return {
        "body": "Records added successfully!"
    }