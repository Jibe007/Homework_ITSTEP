import json

def parse_json(file_name):
    try:
        with open(file_name, 'r') as file:
            data = json.load(file)
            print(f"File: {file_name}\nData: {data}\n")
    except Exception as e:
        print(f"Error reading {file_name}: {e}")
