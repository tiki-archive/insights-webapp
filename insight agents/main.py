import logging
import boto3
from botocore.exceptions import ClientError
import os
import requests
import json



KGRAPH_URL = "https://tiki-insights.s3.us-east-2.amazonaws.com/api_response.json"
BUCKET_NAME = "tiki-insights"


# Connect to API and build insight

# TODO: Authentication w/ kgraph

response = requests.get(KGRAPH_URL).json()

# Build specific insight data from response... see samples/most_frequent_subjects to see what we're building
insight_data = []

totalEmails = 0
for subject in response:
    result = subject[0]
    totalEmails += result["occurrences"]

for subject in response:
    result = subject[0]

    insight_data.append({
        "key": result["subject"],
        "value": round(100 * result["occurrences"] / totalEmails)
    })

# build insight using specific data
insight = {'chart_type': 'PIE', 'chart_data': [
    {
        "filter": "Last 24 Hours",
        "data": insight_data
    }
]}
insight_as_json = json.dumps(insight)

print(insight_as_json)

# Upload to S3
s3 = boto3.resource('s3')
s3.Bucket(BUCKET_NAME).put_object(Key='companies/amazon/most_frequent_subjects.json', Body=insight_as_json)

# Upload a new file
# data = open('samples/most_frequent_subjects.json', 'rb')
