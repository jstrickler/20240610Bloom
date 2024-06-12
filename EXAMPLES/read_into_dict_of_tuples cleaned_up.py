from pprint import pprint
import logging

DATA_FILE_PATH = "../DATA/knxights.txt"

def main():
    """
    Program entry point. 

    Displays data from knights file
    """
    data = read_data(DATA_FILE_PATH)
    pretty_print(data)
    print()
    print_knights(data)
    print()
    print(get_value(data, 'Robin', 2))


def read_data(file_path):
    """
    Read data from knights.txt and return
    a dictionary indexed by the name
    """
    info = {}  # create empty dict

    try:
        with open(file_path) as knights_in:
            for line in knights_in:
                name, title, color, quest, comment = line.rstrip('\n\r').split(":")
                info[name] = title, color, quest, comment  # create new dict element with name as key and a tuple of the other fields as the value
    except IOError as err:
        logging.error(err)
        exit()

    return info

def pretty_print(knight_info):
    """
    Pretty-print all knight data
    """
    pprint(knight_info)

def print_knights(knight_info):
    """
    Print all knights with their titles
    """
    for name, info in knight_info.items():
        print(info[0], name)

def get_value(knight_info, knight_name, field_number):
    """
    Return one value for a particular knight
    """
    return knight_info[knight_name][field_number]

main()