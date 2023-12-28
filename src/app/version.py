import json

version = '''
{
    "release": 1,
    "feature": 2,
    "fix": 2
}
'''

data = json.loads(version)

def get_version():
    return f'{data["release"]}.{data["feature"]}.{data["fix"]}'