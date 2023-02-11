import os


def find_path(name_file):
    abs_path = __file__.split("\\")
    print(abs_path)
    del abs_path[-1]
    print(abs_path)
    del abs_path[-1]
    print(abs_path)
    abs_path = '/'.join(abs_path)
    print(abs_path)
    abs_path = os.path.join(abs_path, name_file)
    print(abs_path)
    return abs_path


# find_path(name_file="images/image.jpeg")