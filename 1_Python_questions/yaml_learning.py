import yaml

# Example data as a Python dictionary
data = {
    'name': 'John Doe',
    'age': 30,
    'city': 'Example City',
    'skills': ['Python', 'JavaScript', 'SQL']
}

# Writing to a YAML file
# with open('example.yaml', 'w') as yaml_file:
#     yaml.dump(data, yaml_file, default_flow_style=False)

# Reading from a YAML file
with open('../example.yaml', 'r') as yaml_file:
    loaded_data = yaml.load(yaml_file, Loader=yaml.FullLoader)

# Print the loaded data
print(loaded_data)
