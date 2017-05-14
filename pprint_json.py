import json
import os.path
import sys


def find_path():
    input_json_directory = sys.argv[1]
    return input_json_directory


def load_json(json_filepath):
    with open(json_filepath, 'r') as json_open:
        json_read = json_open.read()
    return json_read


def prettify_json(json_data):
    prettify_json.decode_ = json.loads(json_data)
    prettify_json_text = json.dumps(prettify_json.decode_,
                                    sort_keys=True, indent=4,
                                    ensure_ascii=False)
    print(prettify_json_text)


if __name__ == '__main__':
    path_find = find_path()
    load_data = load_json(path_find)
    prettify_text = prettify_json(load_data)
