with open('puzzle2_input.txt', 'r') as f:
    puzzle_list = [line.strip() for line in f]
    # print puzzle_list
# puzzle_list = ['abcde', 'fghij', 'klmno', 'pqrst', 'fguij', 'axcye', 'wvxyz']
double_list= []
triple_list = []

# for i in puzzle_list:
#     for char in i:
#         # print i
#         if i.count(char) == 2:
#             if i not in double_list:
#                 double_list.append(i)
#             # print double_list
            
#         if i.count(char) == 3:
#             if i not in triple_list:
#                 triple_list.append(i)
#             # print triple_list

# print len(double_list)
# # print double_list
# print len(triple_list)
# # print triple_list
# checkSum = len(double_list) * len(triple_list)
# print checkSum

new_list= []
# count = 0
for i in puzzle_list:
    for j in puzzle_list:
        if i != j:
            count = 0
            for a,b in zip(i, j):
                if a != b:
                    continue
                if a == b:
                    count += 1
                    if count < len(i) and count > len(i) - 2:
                        if i not in new_list:
                            new_list.append(i)
                            new_list.append(j)
print new_list