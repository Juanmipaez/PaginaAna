while True:
    fname = input("Enter file name: ")
    try:
        file_open = open(fname)
        break
    except:
        print(f'Unable to open "{fname}", try again')
        continue
counter = 0

for line in file_open:
    if line.startswith("From "):
        list0 = line.split()
        counter += 1 
        print(list0[1])
print(f'There were {counter} lines in the file that started with From as the first word')