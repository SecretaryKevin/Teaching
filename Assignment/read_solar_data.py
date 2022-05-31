def is_valid_line_data(line_data_tuple):
    is_vaild = True
    for data in line_data_tuple:
        if data == -1 or data == "-1":
            is_vaild = False
    return is_vaild


def data_tuple_from_line(line_str):
    split_line = line_str.split(",")
    split_line[2] = float(split_line[2])
    split_line[3] = float(split_line[3])
    split_line[4] = float(split_line[4])
    split_line[6] = split_line[6].title()
    return tuple(split_line)


def read_solar_data(filename):
    file = open(filename, 'r')
    lines = file.readlines()
    tuple_list = []
    for line in lines:
        if line != lines[0]:
            line = data_tuple_from_line(line)
            if is_valid_line_data(line):
                tuple_list.append(line)
    return tuple_list


from pprint import pprint
filename = 'data_skinny_10.txt'
full_data_list = read_solar_data(filename)
print(len(full_data_list))
pprint(full_data_list, width=80)
