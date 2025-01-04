import csv


# with open('test.csv', 'w') as csv_file:
#     writer = csv.writer(csv_file)
#     writer.writerow(['user_id', 'user_name', 'comments_qty'])
#     writer.writerow([5235, 'Vova', 1352])
#     writer.writerow([4428, 'Mike', 246])
#     writer.writerow([1684, 'Alice', 73])

with open('test.csv', 'r') as csv_file:
    reader = csv.reader(csv_file)
    print(reader)
    print(type(reader))
    for line in reader:
        print(line)
    # csv_list = list(reader)
    # print(csv_list) список списков
    print(reader.line_num)