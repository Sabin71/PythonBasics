file_rel_path ="./data/flavors.txt"
new_flavors = []
with open(file_rel_path,'a')as file_obj:
    new_flavors = ("\nbanana","\npineapple","\noreo")
    for flavors in new_flavors:
        file_obj.write(flavors)
