import yaml

f = open('mongo.yaml', mode='r')
a = yaml.safe_load(f)
print(a['services']['mongo']['ports'])

# ____________________________________________________________

data = {
    'name': 'John',
    'age': 30,
    'city': 'New York'
}

file_path = 'data.yaml'

with open(file_path, 'w') as yaml_file:
    yaml.safe_dump(data, yaml_file)

print(f"Data has been written to {file_path} using safe_dump")
