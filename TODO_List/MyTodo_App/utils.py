import json

def is_json(data):
    try:
        p_data=json.loads(data)
        valid = True
    except ValueError:
        valid = False
    return valid
