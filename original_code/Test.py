import yaml  # This may need installed as pyyaml
''''
with open('my_config.yaml') as yaml_file:
    my_data = yaml.safe_load(yaml_file)
print(my_data)
'''
def YAML(path):
    with open(path) as yaml_file:
        print(yaml_file)
        my_data = yaml.safe_load(yaml_file)
    print(my_data)

YAML('my_config.yaml')