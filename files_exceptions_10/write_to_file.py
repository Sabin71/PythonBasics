from utilities import *


# with open(file_path, 'a') as file_obj:
#     for line in lines:
#         file_obj.write(line)
#     return file_obj

# option2: with loop
flavors_rel_path = "./data/flavors.txt"
new_flavors = ["banana", "\npineapple", "\noreo"]
write_txt_file(flavors_rel_path, new_flavors, mode='w')

more_flavors = ["\ncherry", "\norange", "\nitalian"]
write_txt_file(flavors_rel_path, more_flavors)

students_rel_path = "./data/students.txt"
new_students = ["Busra", "\nRustam", "\nNatalia"]
write_txt_file(students_rel_path, new_students, mode='w')

more_students = ["\nYuling", "\nLanda", "\nParizod"]
write_txt_file(students_rel_path, more_students, mode='a')
