import yaml


def write_txt_file(file_path, lines, mode="a"):
    """
    Writes to list of inputs as lines to a given file path.
    :param file_path: absolute or relative path of the file
    :param lines: list of information, in the form of List DS
    :return: file object
    """
    with open(file_path, mode=mode) as file_obj:
        for line in lines:
            file_obj.write(line)
        return file_obj

def read_text_file(file_path):
    """
    Reads regular text file
    :param file_path: abs or relative path
    :return: contents in the form of List ds
    """
    print("3. Reading the file by creating list of lines")
    with open(file_path) as file_obj:
        lines = file_obj.readlines()
    return lines

def read_yaml_file(file_path):
    """
    Reads yaml type files (configuration files)
    :param file_path: provide abs or relative path
    :return: data from the yaml file as Dictionary DS
    """
    with open(file_path, 'r') as file:
        data = yaml.safe_load(file)
        return data

def hello_world():
    print("Hello World!")