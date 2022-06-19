"""doc s"""
def data_tuple_from_line(line_str):
    """data from line"""
    split_line = line_str.split(",")
    split_line[2] = float(split_line[2])
    split_line[3] = float(split_line[3])
    split_line[4] = float(split_line[4])
    split_line[6] = split_line[6].title()
    return tuple(split_line)

def is_valid_line_data(line_data_tuple):
    """doc s"""
    is_valid = True
    for data in line_data_tuple:
        if data == -1 or data == "-1":
            is_valid = False
    return is_valid

def read_solar_data(filename):
    """doc s"""
    infile = open(filename)
    contents = infile.read()
    infile.close()
    lines = contents.splitlines()
    tuple_list = []
    for line in lines:
        if line != lines[0]:
            line = data_tuple_from_line(line)
            if is_valid_line_data(line):
                tuple_list.append(line)
    return tuple_list

def installs_by_state(solar_data):
    """doc s"""
    final_dict = {}
    for data in solar_data:
        if data[-1] in final_dict:
            final_dict[data[-1]] += 1
        else:
            final_dict[data[-1]] = 1
    return final_dict

def installs_by_year(solar_data):
    """doc s"""
    final_dict_years = {}
    for data in solar_data:
        year = int(data[1][:4])
        if year in final_dict_years:
            final_dict_years[year] += 1
        else:
            final_dict_years[year] = 1
    return final_dict_years

def total_kw_by_year(solar_data):
    """doc string"""
    final_dict_years_total = {}
    for data in solar_data:
        year = int(data[1][:4])
        if year in final_dict_years_total:
            final_dict_years_total[year] += data[2]
        else:
            final_dict_years_total[year] = data[2]
    return final_dict_years_total


def average_net_cost_per_kw(solar_data):
    """doc string"""
    net_cost_per_kw={}
    for data in solar_data:
        kw = total_kw_by_year(solar_data)
        year = installs_by_year(solar_data)
        pprint(kw)
        pprint(year)


from pprint import pprint
solar_data = read_solar_data("data_20_a.txt")
result = average_net_cost_per_kw(solar_data)
pprint(result, width=15, sort_dicts=False)
