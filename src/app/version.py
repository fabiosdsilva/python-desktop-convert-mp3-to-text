import json

version = '''
{
    "release": 1,
    "feature": 2,
    "fix": 3
}
'''

data = json.loads(version)

def get_version():
    return f'{data["release"]}.{data["feature"]}.{data["fix"]}'