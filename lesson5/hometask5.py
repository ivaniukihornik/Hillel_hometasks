# Завдання 1
# Макс 40 балів
# написати програму, яка просить в користувача ввести через пробіл міста, в яких він був за минулі 10 років
# потім окремо запросити у користувача міста, куди він хоче поїхати внаступні 10 років
# вивести на екран повідомлення з текстом про те, що користувачу, мабуть, дуже сподобалося в містах, які він повторив в
# двох циклах вводу, а саме... (сформувати строку, використовуючи join)
# якщо повтору не було - вивести повідомлення, що користувач відкритий до чогось нового
#
# врахувати випадки, що користувач нічого не вводить не потрібно, в даному випадку вам явно зазначено,
# що ці перевірки не потрібні.
# не потрібно перевіряти введення цифр
# ми виходим із того, що користувач введе щось на зразок "Київ Тернопіль париЖ акапулько-80"
#
# В той же час врахуйте, що користувач може вводити дані в різних регістрах
#
# використати сети!!!

print('Task 1')
visited_cities = set(input('Будь ласка, введіть міста, у яких ви були за минулі 10 років (через пробіл): ').title().split(' '))
desired_cities = set(input('Також введіть міста, які ви бажаєте відвідати за наступні 10 років: ').title().split(' '))
all_cities = visited_cities.union(desired_cities)
matched_cities = set()
for city in all_cities:
    if visited_cities.__contains__(city) and desired_cities.__contains__(city):
        matched_cities.add(city)
matched_cities_str = ', '.join(matched_cities)
print(f'Вам напевне дуже сподобалося в містах: {matched_cities_str}')


# Завдання 2
# макс 60 балів
# зауважте, що значення, що зберігається в кожному елементі - теж словник, і доступ до вкладеного списку
# здійснюється за механізмом
# student[outer_dict_key][inner_dict_key]
#
# Є дані студентів (комбінація імені та прізвища унікальна), що зберігаються за допомогою словника
# 1 - програмно добавити одного студента, з заповненням усіх полів (вік - від 18 до 40, цілочисельне значення,
#     бал від 0 до 100 (інт чи флоат)
# 2 - створити і вивести на екран список студентів (імя та прізвище та середній бал), у яких середній бал більше 90
#     сам формат наповнення цього списку up to you
# 3 - визначити середній бал по групі
# 4 - при відсутності номеру телефону у студента записати номер батьків (номер на ваш вибір)
#
# не забувайте виводити інформаційні повідомлення щодо інформації, яку ви виводите


print('\nTask 2')
import pprint
students = {
    'Іван Петров': {
        'Пошта': 'Ivan@gmail.com',
        'Вік': 14,
        'Номер телефону': '+380987771221',
        'Середній бал': 95.8
    },
    'Женя Курич': {
        'Пошта': 'Geka@gmail.com',
        'Вік': 16,
        'Номер телефону': None,
        'Середній бал': 64.5
    },
    'Маша Кера': {
        'Пошта': 'Masha@gmail.com',
        'Вік': 18,
        'Номер телефону': '+380986671221',
        'Середній бал': 80
    },
}
student_name = input('Прибув новий студент. Введіть, будь ласка, його дані нижче.\nІм\'я та прізвище: ')
while True:
    same_students = False
    for name in students:
        if student_name == name:
            student_name = input('Такий студент вже є. Введіть нового: ')
            same_students = True
            break
    if same_students is False:
        break
mail = input('Пошта: ')
age = int(input('Вік (від 18 до 40): '))
mobile = input('Номер телефону: ')
avg_mark_str = input('Середній бал (від 0 до 100): ')
if avg_mark_str.count('.') > 0:
    avg_mark = float(avg_mark_str)
else:
    avg_mark = int(avg_mark_str)
students.update({
    student_name: {
        'Пошта': mail,
        'Вік': age,
        'Номер телефону': None if len(mobile) == 0 else mobile,
        'Середній бал': avg_mark
    }
})

good_students = dict()
for student in students.items():
    if student[1]['Середній бал'] > 90:
        good_students.update({
            student[0]: student[1]['Середній бал']
        })
print(f'\nСписок відмінників, у кого середній бал більше 90: {good_students}')

total_mark_points = 0
students_count = 0
for student in students.items():
    total_mark_points += student[1]['Середній бал']
    students_count += 1
avg_mark = round((total_mark_points / students_count), 2)
print(f'\nСередній бал групи: {avg_mark}')

for student in students:
    if students[student]['Номер телефону'] is None:
        students[student]['Номер телефону'] = input(f'\nУ студента {student} нема номеру телефону. Введіть номер когось'
                                                    f' із батьків: ')

print('\nОновлений список студентів:')
pprint.pprint(students)