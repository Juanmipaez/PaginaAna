while True:
    fname = input("Enter file name: ")
    try:
        file_open = open(fname)
        break
    except:
        print(f'Unable to open "{fname}", try again')
        continue

list0 = []

for line in file_open:
    line = line.rstrip()
    list1 = line.split()
    for word in list1:
        list0.append(word)

counts = {}
for words in list0:
    counts[words] = counts.get(words, 0) + 1
print(counts)

num_list = []
for keys in counts:
    num_list.append(counts[keys])
largest_num = max(num_list)


print("The most repeated word/s is/are: ")
for keys in counts:
    if counts[keys] == largest_num:
        print(f'{keys} : {largest_num}')