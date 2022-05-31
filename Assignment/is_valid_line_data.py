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


line = 'SCE-INT-500025441,2011-09-23,4.48,35175,4094,90254,Hermosa Beach,CA'
data_tuple = data_tuple_from_line(line)
result = is_valid_line_data(data_tuple)
print(result)
