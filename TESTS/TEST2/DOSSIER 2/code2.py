import os

def list_files(folder):
    return os.listdir(folder)

def create_folder(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)


def create_file(path, content):
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
def read_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()
    
