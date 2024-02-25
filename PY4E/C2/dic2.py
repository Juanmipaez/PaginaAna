names = ["Juan", "Dani", "Emma","Emma", "Emma","Juan"]
counts = {}
largest = None

for name in names:
    counts[name] = counts.get(name, 0) + 1
print(counts)

num_list = []
for value in counts:
    num_list.append(counts[value])
largest = (max(num_list))

for value in counts:
    if counts[value] == largest:
        print(f'The word {value} is one of the most repeated words, with a count of {largest}')

