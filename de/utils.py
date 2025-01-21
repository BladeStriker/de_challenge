import yaml

def load_queries(yaml_file):
    with open(yaml_file, 'r') as file:
        queries = yaml.safe_load(file)
    return queries['queries']