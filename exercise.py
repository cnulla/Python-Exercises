#Number One
list_of_persons = ["Camille", "Angelica", "Kyle", "Manny", "Earvin", "Mimi"]
my_dictionary = {}

for person in list_of_persons:
    key = len(person)
    if key not in my_dictionary:
        my_dictionary[key] = []
    my_dictionary[key].append(person)
# print my_dictionary


#Number Two
my_list = [1,2,3]
def insert_list(number):
    my_list.insert(0,number)

#insert_list(5)
#insert_list(7)


#Number Three
odd_list = []
for odd in range(1,50):
    if odd % 2 != 0:
        odd_list.append(odd)
#print odd_list


#Number Four
new_list1 = [1,2,3,4]
convert_list = int("".join(map(str, new_list1)))
#print convert_list


#Number Five
sort_numbers = [8,7,4,6,11,15,8]
sort_numbers.sort()
#print sort_numbers


#Number Six
empty_list = []
#if not empty_list:
   # print 'empty'
#else:
   # print 'is not empty'


#Number Seven
def convert_arrays_to_dictionary(my_array):
    new_list2 = {}
    for every_index in my_array:
        new_list2[every_index[0]] = every_index[1]

arr = [['Camille','Nulla'], ['Rayvince', 'Parages']]
#print convert_arrays_to_dictionary(arr)


#Number Eight
def remove_duplicate(duplicate):
    not_duplicate = list(set(duplicate))
    return not_duplicate

sample_list = [1,1,2,3,5,6,5]
#print remove_duplicate(sample_list)

#Number Nine
def return_unique(unique):
    unique_list = []
    for every in unique:
        if every not in unique_list:
            unique_list.append(every)
            return unique_list
dup_list = [1,2,1]
#print return_unique(dup_list)


#Number Ten
def find_index(my_list,my_index):
    return my_list.index(my_index)


#Number Eleven




#Number Twelve
def val_contain(my_list, value):
        if value in my_list:
            return True




