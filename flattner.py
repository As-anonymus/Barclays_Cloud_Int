import json

def flatten_json(nested_json, parent_key='', sep='_'):
    """
    Flatten a nested JSON object.

    Parameters:
    - nested_json (dict): The nested JSON object to flatten.
    - parent_key (str): The parent key of the nested JSON object.
    - sep (str): The separator to use between keys.

    Returns:
    - dict: The flattened JSON object.
    """
    flattened_json = {}
    for key, value in nested_json.items():
        new_key = parent_key + sep + key if parent_key else key
        if isinstance(value, dict):
            flattened_value = flatten_json(value, new_key, sep=sep)
            flattened_json.update(flattened_value)
        else:
            flattened_json[new_key] = value
    return flattened_json

with open('BankCustomerData.json', 'r') as f:
    nested_json = json.load(f)
flattened_json = flatten_json(nested_json)
print(json.dumps(flattened_json, indent=4))
