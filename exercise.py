string_list = []
dimensions = []
line_list = []
with open('key.txt', 'r') as file:
    for line in file:
        num = int(line)
        dimensions.append(num)
    col = dimensions[0]
    row = dimensions[1]

with open('secret.txt', 'r') as file1:
    for line in file1:
        line.strip()
        line_list += line.split()

with open('public.txt', 'w') as file2:
    line_num = 0
    row_num = 0
    while line_num < len(line_list):
        for i in range(row):
            for j in range(col):
                file2.write(line_list[line_num])
                line_num += 1
            row_num += 1
            if row_num < row:
                file2.write("\n")