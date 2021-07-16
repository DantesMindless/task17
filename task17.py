# task1
import unittest


class Test(unittest.TestCase):

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])

    def test_math(self):
        m = 13 + 13
        self.assertEqual(m, 13 * 2)

    def test_cap(self):
        self.assertEqual('ron'.capitalize(), 'Ron')

    def test_for(self):
        l = [1, 2, 3, 4, 5]
        l1 = [n ** 2 for n in l]
        self.assertEqual(l1, [1, 4, 9, 16, 25])


# task2


import json

phonebook = {}
phonebook['Mary Jork'] = [{'First name': 'Mary',
                           'Last name': 'Jork',
                           'City': 'Berlin',
                           'Phone number': 99999999}]

phonebook['Steve Hudson'] = [{'First name': 'Steve',
                              'Last name': 'Hudson',
                              'City': 'London',
                              'Phone number': 88888888}]
class Testphonebook(unittest.TestCase):
    def test_2(self):
        self.assertEqual(type(phonebook),dict)
    def test_search_by_fullname(self):
        fullname_input = input('Enter full name ')
        for k in phonebook:
            if k == fullname_input:
                print(phonebook[k])



    def test_search_by_name(self):
        name_input = input('Enter name ')

        for k in phonebook:
            for v in phonebook[k]:
                if v['First name'] == name_input:
                    print(v)


    def test_search_by_lastname(self):
        lastname_input = input('Enter lastname ').capitalize()

        for k in phonebook:
            for v in phonebook[k]:
                if v['Last name'] == lastname_input:
                    print([v])


    def print_phonebook(self):
        with open('pb.json') as phonebook_file:
            print(phonebook_file.read())


    def test_search_by_phonenumber(self):
        phonenumber_input = int(input('Enter phonenumber '))

        for k in phonebook:
            for v in phonebook[k]:
                if v['Phone number'] == phonenumber_input:
                    print(v)


    def test_search_by_city(self):
        city_input = input('Enter city ').capitalize()

        for k in phonebook:
            for v in phonebook[k]:
                if v['City'] == city_input:
                    print(v)


    def test_add_new_entry(self):
        entry_name_input = input('Enter name ').capitalize()
        entry_lastname_input = input('Enter lastname ').capitalize()
        while ValueError:
            try:
                entry_number_input = int(input('Enter number '))
                break
            except ValueError:
                print('Numbers only')
        entry_city_input = input('Enter city ').capitalize()
        phonebook[entry_name_input + ' ' + entry_lastname_input] = [{'First name': entry_name_input,
                                                                     'Last name': entry_lastname_input,
                                                                     'City': entry_city_input,
                                                                     'Phone number': entry_number_input}]


    def delete(self):
        delete_input = input('Enter full name of whom you want to remove from the list ')

        for k in phonebook:
            if delete_input in k:
                phonebook.pop(k)
                break


    def update(self):
        delete_input = input('Enter full name of whom you want to update ')

        for k in phonebook:
            if delete_input in k:
                phonebook.pop(k)
                entry_name_input = input('Enter name ').capitalize()
                entry_lastname_input = input('Enter lastname ').capitalize()
                while ValueError:
                    try:
                        entry_number_input = int(input('Enter number '))
                        break
                    except ValueError:
                        print('Numbers only')
                entry_city_input = input('Enter city ').capitalize()
                phonebook[entry_name_input + ' ' + entry_lastname_input] = [{'First name': entry_name_input,
                                                                             'Last name': entry_lastname_input,
                                                                             'City': entry_city_input,
                                                                             'Phone number': entry_number_input}]
                break

if __name__ == '__main__':

 unittest.main()
# operation = ''
# while operation != '1':
#     with open('pb.json', 'w') as phonebook_file:
#         json.dump(phonebook, phonebook_file)
#
#     operation = input(
#         "exit = 1\nsearch by fullname = 2\nsearch by name = 3\nsearch by lastname = 4\nsearch by phonenumber = 5\nsearch by city = 6\ndelete = 7\nadd new entry = 8\nprint phonebook = 9\nupdate = 10\n").lower()
#     if operation == '2':
#         search_by_fullname()
#     elif operation == '9':
#         print_phonebook()
#     elif operation == '8':
#         add_new_entry()
#     elif operation == '3':
#         search_by_name()
#     elif operation == '4':
#         search_by_lastname()
#     elif operation == '5':
#         search_by_phonenumber()
#     elif operation == '7':
#         delete()
#     elif operation == '6':
#         search_by_city()
#     elif operation == '10':
#         update()
# if __name__ == '__main__':
#
#  unittest.main()
