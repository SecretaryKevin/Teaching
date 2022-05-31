
def data_tuple_line(line_str):
    split_line = line_str.split(",")
    split_line[2] = float(split_line[2])
    split_line[3] = float(split_line[3])
    split_line[4] = float(split_line[4])
    split_line[6] = split_line[6].title()
    return tuple(split_line)


line = 'SCE-INT-500025441,2011-09-23,4.48,35175,4094,90254,TEST TEST,CA'
data = data_tuple_line(line)
print(data)
