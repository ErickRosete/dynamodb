import boto3
from datetime import datetime
from decimal import Decimal
import json

#EE.UU. Este (Ohio)	us-east-2	rds.us-east-2.amazonaws.com	HTTPS
#EE.UU. Este (Norte de Virginia)	us-east-1	rds.us-east-1.amazonaws.com	HTTPS
#EE.UU. Oeste (Norte de California)	us-west-1	rds.us-west-1.amazonaws.com	HTTPS
#EE.UU. Oeste (Oregón)	us-west-2	rds.us-west-2.amazonaws.com	HTTPS
dynamodb = boto3.resource('dynamodb', region_name ='us-east-2' )

table = dynamodb.Table('SmartLabs')
print(table.creation_date_time)


now = datetime.now()
timestamp = str(now)
#timestamp = datetime.timestamp(now)

item={
        'Indice': 1,
        'Identificación': 'Lab-Rob',
        'Parameter': 'Humidity',
        'TimeStamp': timestamp,
        'Valor': 30
    }

item_dump = json.dumps(item)
item = json.loads(item_dump, parse_float=Decimal)
table.put_item(Item = item)