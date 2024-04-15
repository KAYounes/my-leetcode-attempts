import json


def print_dict(_dict, identifier='dict'):
    json_data = json.dumps(_dict, indent=4)

    print(identifier, sep="", end=" =\n")
    print(json_data)