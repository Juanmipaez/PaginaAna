file = open("Mbox.txt")
counter = 0
float_addition = 0
for line in file:
    if line.startswith("X-DSPAM-Confidence:"):
        float_num = float(line[19:])
        float_addition += float_num
        counter += 1
print(f'Average is: {float_addition/counter}')
