from classes9.exercise9_6 import *
print("READING TEXT FILES")
file_path = "C:/dev/PythonBasics/files_exceptions_10/data/flavors.txt"
file_rel_path ="./data/flavors.txt"
with open("./data/flavors.txt")as file_obj:
    contents = file_obj.read().strip()
print("1.Reading the file as whole.")
print(contents)
print("-------------------")
print("2. Reading the file line by line")




def read_text_file(file_path):
    """ Reads text"""
    print("3.Reading the file by creating list of lines")
    with open(file_path)as file_obj:
        lines = file_obj.readlines()
        return lines
flavors = read_text_file(file_rel_path)
print(flavors)
for flavor in flavors:
        print(f"We have {flavor} ice-cream.")
