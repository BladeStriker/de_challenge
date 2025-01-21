import yaml

def load_queries(yaml_file):
    # Open the YAML file in read mode
    with open(yaml_file, 'r') as file:
        queries = yaml.safe_load(file)
    # Return the 'queries' section of the YAML file
    return queries['queries']