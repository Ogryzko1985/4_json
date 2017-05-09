import json
import os.path
json_file = 'text.txt'
current_file_name = __file__


def find_path():
    dir = os.path.abspath(current_file_name)
    dir1 = os.path.split(dir)
    file_dir = dir1[0] + r'\\'[:-1]+json_file
    return file_dir


def load_data(filepath):
    with open(filepath, 'r') as load_data_read:
        data_loaded = load_data_read.read()
    return data_loaded


def pretty_print_json(data):
    pretty_print_json.decode_ = json.loads(data)
    pretty_print_text = json.dumps(pretty_print_json.decode_,
                                   sort_keys=True, indent=4,
                                   ensure_ascii=False)
    print(pretty_print_text)


if __name__ == '__main__':
    path_finding = find_path()
    data_loading = load_data(path_finding)
    pretty_printing = pretty_print_json(data_loading)
