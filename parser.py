import json
import os
from typing import List, Dict, Any, Optional

def read_json_file(file_path: str) -> Optional[List[Dict[str, Any]]]:
    try:
        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                data = json.load(file)
            return data
        else:
            print(f"{file_path} doesn't exist.")
            return None
    except json.JSONDecodeError as e:
        print(f"Error reading JSON file: {e}")
        return None

def get_json_dict_list(data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    result = []

    for item in data:
        result.append({
            'name': item['name'],
            'age': item['age'],
            'email': item['email'],
            'courses': item['courses'],
            'address': item['address']
        })
    return result

def print_dict_list(dict_list: List[Dict[str, Any]]) -> None:
    for item in dict_list:
        print(item)

def main() -> None:
    file_path = 'data.json'
    data = read_json_file(file_path)

    if data is None:
        return

    json_dict_list = get_json_dict_list(data)
    print_dict_list(json_dict_list)
    
if __name__ == "__main__":
    main()
