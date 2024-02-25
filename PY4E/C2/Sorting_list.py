fname = input("Enter file name: ")
file_open = open(fname)

list0 = list()

for line in file_open:
    line = line.rstrip()
    list1 = line.split()
    for word in list1:
        if word not in list0:
            list0.append(word)
list0.sort()
print(list0)