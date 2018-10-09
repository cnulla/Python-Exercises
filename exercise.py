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
print odd_list

#Number Four
new_list1 = [1,2,3,4]
convert_list = int("".join(map(str, new_list1)))
print convert_list
