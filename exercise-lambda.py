########################################################################
# Function to perform fetching of key/value pair from Parameter Store  #
# and storing in S3 bucket                                             #
########################################################################

#include modules
import boto3
import json

client = boto3.client('ssm')

#define lambda function
def lambda_handler(event, context):

	#fetch key/value pair from parameter store
    response = client.get_parameter(Name='/UserName', WithDecryption=True)
    
	#connect and push data to file in s3 bucket
	s3 = boto3.client('s3')
    bucket ='akriti-personal'
    
    dataToUpload = {}
    dataToUpload['Name'] = response['Parameter']['Name']
    dataToUpload['Value'] = response['Parameter']['Value']
    
    fileName = 'exercise-lambda-file2' + '.json'
    uploadByteStream = bytes(json.dumps(dataToUpload).encode('UTF-8'))
    
    s3.put_object(Bucket=bucket, Key=fileName, Body=uploadByteStream)
    print('Put Complete')