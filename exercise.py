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
def convert_arrays_to_dictionary(my_array):
    new_list2 = {}
    for every_index in my_array:
        new_list2[every_index[1]] = every_index[0]
    return new_list2


arr = [['Camille','Nulla'], ['Rayvince', 'Parages']]
print convert_arrays_to_dictionary(arr)

