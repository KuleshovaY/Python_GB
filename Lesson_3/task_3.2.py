# Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.


def data_func(name, surname, year_born, city, email, phone):
    return (name, surname, year_born, city, email, phone)

print(data_func(name= 'Sabrina', surname= 'Simon', year_born= '1989', c
                ity= 'New York', email= 'sambrina.s@gmail.com',
                phone= '+18239-234-34-12'))


# вариант решения
def print_data(**kwargs):
    return ' '.join(kwargs.values())
print(print_data(name=input('Enter your name'), surname=input('Enter your surname'),
                 birth_year=input('Enter your year of birth'),
                 city=input('Enter your city'), email=input('Enter your email'),
                 phone=input('Enter your phone number')))


#вариант решения
def print_data(name, surname, birthday, city, email, phone):
    return f'Name - {name}, surname - {surname}, birthday - {birthday}, city - {city},'\
           f'email - {email}, phone - {phone}'
print(prin_data(name= 'Sabrina', surname= 'Simon', year_born= '1989',
                city= 'New York',email= 'sambrina.s@gmail.com',
                phone= '+18239-234-34-12'))
