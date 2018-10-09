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
if not empty_list:
    print 'empty'
else:
    print 'is not empty'


#Number Seven
def convert_arrays_to_dictionary(my_array, my_array1):
    new_zip = zip(my_array,my_array1)
    dictwords = dict(new_zip)
    return dictwords

arr = ['Camille','Nulla']
arr2 = ['Rayvince', 'Parages']
#print convert_arrays_to_dictionary(arr,arr2)


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
def find_object(my_dictionary, object):
    new_dict = my_dictionary.index(object)
    return new_dict


#Number Twelve
def val_contain(my_list, value):
        if value in my_list:
            return True


#Number Thirteen
def check_difference(my_list1,my_list2):
    new_list3 = []
    for every in my_list1:
        if every not in my_list2:
            new_list3.append(every)
    return new_list3


#Number Fourteen
def remove_non_integer(my_list):
    new_list = []
    for every in my_list:
        if every.isdigit():
            new_list.append(every)
    return new_list


#Number Fifteen
given_list = ['a','b','c']
given_list2 = ['x','y','z']

print given_list[0] + given_list2[0]
print given_list[1] + given_list2[1]
print given_list[2] + given_list2[2]


#Number Sixteen
new_string = '1234'
new_list5 = []
convert_list1 = str(new_list5.append(int(new_string)))
#print convert_list1

