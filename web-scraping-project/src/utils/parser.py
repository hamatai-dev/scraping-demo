def format_data_to_json(data):
    import json
    return json.dumps(data, ensure_ascii=False, indent=4)