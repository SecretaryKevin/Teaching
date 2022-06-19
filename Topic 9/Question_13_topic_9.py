MOUNTHS = {1: "Jan", 2: "Feb", 3: "Mar", 4: "Apr", 5: "May", 6: "Jun",
           7: "Jul", 8: "Aug", 9: "Sep", 10: "Oct", 11: "Nov", 12: "Dec"}


def generate_daily_totals(filename, output_filename):
    """doc s"""
    """open file"""
    infile = open(filename)
    contents = infile.read()
    infile.close()
    lines = contents.splitlines()
    """create empty list and formats the data"""
    final_data = []
    for line in lines:
        data = line.split(",")
        date = data.pop(0)
        year, month, day = date.split("-")
        daily_total = 0
        for item in data:
            daily_total += float(item)
        final_data.append((f"{day} {MOUNTHS[int(month)]} {year} = {daily_total:.2f}"))
    """write to file"""
    output_file = open(output_filename, "w")
    for data in final_data:
        output_file.write(data + "\n")
    output_file.close()


generate_daily_totals("added text file here", "output.txt")
