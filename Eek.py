import os

def new(name):
    if (name):
        x = os.path.join('C:', f'EekusGD Community Server/Files/{name}')
        g = os.mkdir(x)
        print(f"Succesfully created {name}")
    else:
        print("File is not created.\nReason: null folder cannot be created.")
    def remove(file):
        if file == name:
            os.remove(x)
            print("Succesfully removed.")
        else:
            print("No file found.")