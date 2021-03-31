def add(x, y):
    """
    :type x: object
    :type y: object
    """
    return x + y


def write(f_path, data_in):
    with open(f_path, "w") as file_in:
        file_in.write(data_in)
