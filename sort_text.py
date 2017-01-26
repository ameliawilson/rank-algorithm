##############################################################################
# Take rank text file, sort it
##############################################################################
print("This program sorts a rank text file")
file_name = input("Please Enter File Name: ")
input_file = open(file_name, 'r')
first_line = input_file.readline() # skip first line
first_line = first_line.strip('\n')

categories = first_line.split(',')
for i in range(len(categories)):
    print(i, categories[i])
    
j = int(input("Sort by what category? Enter the number: "))    
d = {}

for line in input_file: 
    line = line.strip('\n')
    info = line.split(',')
    try:
        key = info[j]+info[0]
        d[key] = line
    except IndexError:
        print("idk why this isn't working")
        
key_list = list(d.keys())
key_list.sort()
key_list.reverse()
#print(key_list)
input_file.close()

new_file = open(file_name, 'w')
print(first_line, file=new_file)
for i in key_list:
    print(d[i], file=new_file)
new_file.close()