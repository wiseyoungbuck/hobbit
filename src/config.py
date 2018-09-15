from ruamel.yaml import YAML

def load(file='config.yaml'):
    yaml = YAML(typ='safe')
    with open(file) as f:
        config = yaml.load(f)
    return config

