'''
flow goes open => do something => close
'''

# barent_file = open('barent.txt') # open the barent.txt file REMEMBER TO CLOSE
# print(barent_file.read()) # read what is inside of that file
# barent_file.close() # close the file once finished

# 'r' read 'r+' read and write 'w' write 'a' append
# barent_file = open('barent.txt', 'a') # open the file to append to it
# barent_file.write('\ntesting\n') # write to the file
# barent_file.close()

# barent_file = open('barent.txt', 'a')
# numbers = [1, 2, 3]
# for i in range(len(numbers)):
#   num = numbers[i]
#   barent_file.write('\n{}'.format(num))
# barent_file.close()

# with open w, if the file does not exist, it will be created
# super fucking cool
adam_file = open('adam.txt', 'r+')
print(adam_file.readlines())
adam_file.close()

# num_file = open('nums.txt', 'r+')
# # print(num_file.readlines())

# count=0
# for line in num_file:
#   # count+=1
#   print('Line {}: {} '.format(count, line.strip()))
#   count += int(line)
# num_file.close()

# gotta split on \n 
# new_file = open('new_file.txt')
# file_items = new_file.readlines()

# for i in range(len(file_items)):
#   each_item = file_items[i]
#   # print('BEFORE : {}'.format(each_item))
#   # print(each_item[0:-1])
#   file_items[i] = each_item[0:-1]
#   print('FILE ITEMS : ', file_items)

# # print('These are the file items: {}'.format(file_items))
# new_file.close()
