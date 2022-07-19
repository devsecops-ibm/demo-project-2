import json
import os
import boto3

json_data = '[{"ID":10,"Name":"Pankaj","Role":"CEO"},' \
            '{"ID":20,"Name":"Jayden","Role":"CISO"},' \
            '{"ID":30,"Name":"David","Role":"Editor"}]'

json_object = json.loads(json_data)
json_formatted_data = json.dumps(json_object, indent=2)
print(json_formatted_data)