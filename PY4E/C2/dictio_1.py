names = []
while True:
    get_name = input("Enter name: ").capitalize()
    if get_name == "Done":
        break
    names.append(get_name)
if len(names) == 0:
    print("There are no elements in the list")
else: 
    print(names)

counts = {}

for name in names:
    counts[name] = counts.get(name, 0) + 1
if len(counts) == 0:
    print("There are no elements in the dictionary")
else: 
    print(counts)
