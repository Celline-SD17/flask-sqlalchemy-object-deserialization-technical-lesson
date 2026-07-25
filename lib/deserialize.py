# lib/deserialize.py

from marshmallow import Schema, fields
from pprint import pprint

# schema

class HamsterSchema(Schema):
     name = fields.Str()
     breed = fields.Str()
     dob = fields.Date()
hamster_schema = HamsterSchema()
hamster_dict = {"name" : "Fluffernutter", "breed": "Roborovski", "dob" : "2014-08-11"}
result = hamster_schema.load(hamster_dict)
print(type(result)) 
pprint(result)

hamster_json = '{"name": "Wiggles", "breed": "Siberian", "dob": "2020-01-30"}'
result_2 = hamster_schema.loads(hamster_json)
print(type(result_2)) 
pprint(result_2)

hamster_1 = {"name": "Nibbles", "breed": "European",  "dob": "2018-04-30"}
hamster_2 = {"name": "Snuggles", "breed": "Chinese", "dob": "2023-10-07"}
hamster_list = [hamster_1, hamster_2]
result_3 = hamster_schema.load(hamster_list, many = True)
print(type(result_3)) 
pprint(result_3) 

hamster_1 = '{"name": "Honey", "breed": "Turkish", "dob": "2009-06-03"}'
hamster_2 = '{"name": "Squeaky", "breed": "Winter White", "dob": "2022-12-31"}'
hamsters  = f'[{hamster_1}, {hamster_2}]'   #string contains JSON array of objects
hamster_schema_many = HamsterSchema(many=True)
result_4 = hamster_schema_many.loads(hamsters)
print(type(result_4))  # => <class 'list'>
pprint(result_4) 