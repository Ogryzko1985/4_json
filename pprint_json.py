import json
import os.path
def find_path1():
    dir=os.path.abspath(__file__)  
    find_path1.file_dir = dir[:-14]+'text.txt'
    print(find_path1.file_dir)
    return find_path1.file_dir
def load_data(filepath):
    data = open(filepath, 'r')
    load_data.read_ = data.read()  
    return load_data.read_
def pretty_print_json(data):
    pretty_print_json.decode_ = json.loads(data)
    print(json.dumps(pretty_print_json.decode_,sort_keys=True,indent = 4,ensure_ascii=False))
    

if __name__ == '__main__':
    find_path1()
    load_data(find_path1.file_dir)
    pretty_print_json(load_data.read_)
