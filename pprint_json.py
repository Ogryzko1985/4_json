import json
import os.path
def find_path():
    directory=os.path.abspath(__file__)  
    find_path.file_directory = directory[:-14]+'text.txt'
    #print(find_path.file_directory)
    return find_path.file_directory
def load_data(filepath):
    data_to_load = open(filepath, 'r')
    load_data.read_file = data_to_load.read()  
    return load_data.read_file
def pretty_print_json(data_to_prettify):
    pretty_print_json.decode_file = json.loads(data_to_prettify)
    print(json.dumps(pretty_print_json.decode_file,sort_keys=True,indent = 4,ensure_ascii=False))
    

if __name__ == '__main__':
    find_path()
    load_data(find_path.file_directory)
    pretty_print_json(load_data.read_file)
