```python
import boto3

class BackendInfrastructure:
    def __init__(self):
        self.s3 = boto3.resource('s3')
        self.dynamodb = boto3.resource('dynamodb')
        self.backendData = {}

    def create_bucket(self, bucket_name):
        try:
            self.s3.create_bucket(Bucket=bucket_name)
            self.backendData['bucket_name'] = bucket_name
            return True
        except Exception as e:
            print(e)
            return False

    def create_table(self, table_name):
        try:
            table = self.dynamodb.create_table(
                TableName=table_name,
                KeySchema=[
                    {
                        'AttributeName': 'id',
                        'KeyType': 'HASH'
                    },
                ],
                AttributeDefinitions=[
                    {
                        'AttributeName': 'id',
                        'AttributeType': 'N'
                    },
                ],
                ProvisionedThroughput={
                    'ReadCapacityUnits': 5,
                    'WriteCapacityUnits': 5
                }
            )
            self.backendData['table_name'] = table_name
            return True
        except Exception as e:
            print(e)
            return False

    def get_backend_data(self):
        return self.backendData

backend = BackendInfrastructure()
backend.create_bucket('ai-real-estate-advisor')
backend.create_table('property_data')
backendData = backend.get_backend_data()
```