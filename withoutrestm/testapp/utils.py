import json
def is_validjson(json_data):
    try:
        real=json.loads(json_data)
        is_valid=True
    except ValueError:
        is_valid=False
    return is_valid
