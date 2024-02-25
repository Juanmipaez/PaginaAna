while True:
    num_line = int(input("Number or lines you'd like: "))
    col_1 = num_line
    col_2 = num_line
    initial_num = 1
    initial2_num = 0
    
    while col_1 > 0:
        col_1 -= 1
        print (f'{col_1 * " "}{initial_num * "#"} {initial_num * "#"}')
        initial_num += 1
        
    while col_2 > 0:
        col_2 -= 1
        print (f'{initial2_num * " "}{num_line * "#"} {num_line * "#"} ')
        num_line -= 1
        initial2_num += 1

