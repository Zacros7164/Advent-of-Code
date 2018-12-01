with open('puzzle1_input.txt', 'r') as f:
    puzzle_list = [line.strip() for line in f]

temp = 0
total = 0
number_list = []
freq_total= []
rotations = 0
# print puzzle_list
testing= True
for i in puzzle_list:
    number_list.append(int(i))
while testing:
    print rotations
    rotations += 1
    for i in range (0,len(number_list)):
        temp = number_list[i]
        total += temp
        # print total
        if total not in freq_total:
            freq_total.append(total)
        elif total in freq_total:
            print total
            testing = False
            break
       




