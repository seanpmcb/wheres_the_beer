
config = {}

def set_config(in_config):
    for k,v in in_config.items():
        config[k] = v

def get(name):
    if name in config:
        return config[name]
    raise ValueError('unknown config param: %s' % name)
