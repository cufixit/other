import boto3
import json

JSON = "311_data.json"

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamodb.Table('reports')

if __name__ == '__main__':

    with table.batch_writer() as batch:
        with open(JSON) as fp:
            Lines = fp.readlines()
            for line in Lines:
                data = json.loads(line)

                # Convert the lists in the 'keywords' column back to sets
                # Assume sets have been converted into a list of keywords when exported to JSON
                data['keywords'] = set(data['keywords'])

                batch.put_item(Item=data)
