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


def installs_by_state(solar_data):
    final_dict = {}
    for data in solar_data:
        if data[-1] in final_dict:
            final_dict[data[-1]] = final_dict[data[-1]] + data[2]
        else:
            final_dict[data[-1]] = data[2]
    return final_dict


from pprint import pprint
solar_data = read_solar_data('data_100_a.txt')
print(read_solar_data('data_100_a.txt'))
result = installs_by_state(solar_data)
pprint(result, width=15, sort_dicts=False)