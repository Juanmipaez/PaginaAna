while True:
    fname = input("Enter file name: ").capitalize()
    if fname == "quit":
        quit()
    try:
        read_file = open(fname)
        break
    except:
        print(f'File {fname} cannot be opened, plase check file name')
        continue

for line in read_file:
    line = line.rstrip()
    print(line.upper())




