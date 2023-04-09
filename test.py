# class Empty:
#     pass
#
#
# my_list = [
#     ('apple', 23),
#     ('banana', 80),
#     ('cherry', 13),
#     ('date', 10),
#     ('elderberry', 4),
#     ('fig', 65),
#     ('grape', 5),
#     ('honeydew', 7),
#     ('kiwi', 1),
#     ('lemon', 10),
# ]
#
# for i in my_list:
#     name ,amount = i
#     print(setattr(Empty,name,amount))
# import my_package


# class Person:
#     name = "John Smith"
#     age = 30
#     gender = "male"
#     address = "123 Main St"
#     phone_number = "555-555-5555"
#     email = "johnsmith@example.com"
#     is_employed = True
#
#
# text = input().lower().split()
# for i in text:
#     if hasattr(Person, i):
#         print(f'{i} - YES')

#
# class Person:
#     name = "John Smith"
#     age = 30
#     gender = "male"
#     address = "123 Main St"
#     phone_number = "555-555-5555"
#     email = "johnsmith@example.com"
#     is_employed = True
#
#
# print(*[f'{i}-Yes' if hasattr(Person, i.lower()) else f'{i}-NO' for i in input().split()], sep='\n')


# class Config:
#     pass
#
#
# def create_instance(n: int) -> Config:
#     x = Config()
#     for i in range(1, n + 5):
#         setattr(x, 'attribute' + str(i), 'value' + str(i))
#     return x
#
#
# print(create_instance(3).__dict__)
# class Hero():
#
#     def __init__(self, name):
#         self.name = name
#
#     def move(self, direction, distance):
#
#         if direction == "north":
#             print(self.name, "движется", distance, "метров", "на север")
#         elif direction == "south":
#             print(self.name, "движется", distance, "метров", "на юг")
#         elif direction == "west":
#             print(self.name, "движется", distance, "метров", "на запад")
#         elif direction == "east":
#             print(self.name, "движется", distance, "метров", "на восток")
#         else:
#             print(self.name, "движется непонятно куда")


# class Enemy():
#
#     def __init__(self, name):
#         self.name = name
#
#     def move(self, direction, distance):
#
#         directions_list = {"north": "на север", "south": "на юг", "west": "на запад", "east": "на восток"}
#         if direction not in directions_list.keys():
#             print(self.name, "движется непонятно куда")
#         else:
#             print(self.name, "движется", distance, "метров", directions_list[direction])
#
#
# class Character(Hero, Enemy):
#     def all_move(self, direction, distance):
#         self.move(direction, distance)
#         self.move(direction, distance)
#
#
# pythomir = Hero("Питомир")
# bugoonya = Enemy("Багуня")
#
# pythomir.move("north", 50)
# pythomir.move("west", 10)
# pythomir.move("climb", 0)
#
# bugoonya.move("north", 50)
# bugoonya.move("west", 10)
# pythomir.move("climb", 0)
#
# # Не удаляйте код ниже, это проверка!
#
# if not 'Character' in dir():
#     print("Общий класс родитель Character не создан")
#
# if not hasattr(Character, "move"):
#     print("У общего класса отсутствует метод move")
# Напишите определение класса Robot
# class Robot():
#     def set_name(self, name):
#         self.name = name
#
#     def say_hello(self):
#         if hasattr(self, 'name'):
#             print(f'Hello, human! My name is {self.name}')
#         else:
#             print('У робота нет имени')
#
#     def say_bye(self):
#         print('See u later alligator')
#
#
# # Ниже код для проверки класса Robot
#
# c3po = Robot()
# c3po.say_hello()
# c3po.set_name('R2D2')
# c3po.say_hello()
# c3po.say_bye()
# #
# r = Robot()
# r.set_name('Chappy')
# r.say_hello()
#
# d = Robot()
# d.say_hello()
# d.set_name('Wally')
# d.say_hello()

# Напишите определение класса Counter
# class Counter():
#     def start_from(self, count=0):
#         self.count = count
#
#     def increment(self):
#         self.count += 1
#
#     def display(self):
#         print(f'Текущее значение счетчика = {self.count}')
#
#     def reset(self):
#         self.count = 0
#
#
# # Ниже код для проверки класса Counter
#
# c1 = Counter()
# c2 = Counter()
#
# assert isinstance(c1, Counter)
# assert isinstance(c2, Counter)
# assert c1.__dict__ == {}
# assert c2.__dict__ == {}
#
# c1.start_from(45)
# assert len(c1.__dict__) == 1
# c1.increment()
# c1.display()  # печатает 46
# c1.increment()
# c1.display()  # печатает 47
#
# c2.start_from()
# c2.display()  # печатает 0
# c2.increment()
# c2.display()  # печатает 1
#
# c1.reset()  # обнулили с1, но с2 не должен меняться
# c1.display()  # печатает 0
#
# c2.display()  # попрежнему печатает 1

# Напишите определение класса Constructor
# class Constructor():
#     def add_atribute(self, x, y):
#         setattr(self, x, y)
#
#     def display(self):
#         print(self.__dict__)
#
#
# # Ниже код для проверки класса Constructor
#
# obj1 = Constructor()
# assert obj1.__dict__ == {}
# obj1.display()
# obj1.add_atribute('color', 'red')
# assert obj1.color == 'red'
# obj1.add_atribute('width', 20)
# assert obj1.width == 20
# obj1.display()
#
# obj2 = Constructor()
# obj2.display()
# obj2.add_atribute('height', 100)
# assert obj2.height == 100
# obj2.display()
#
# obj3 = Constructor()
# obj3.display()
# obj3.add_atribute('a', 100)
# obj3.add_atribute('b', 300)
# obj3.add_atribute('c', 200)
# obj3.add_atribute('b', 1)
# assert obj3.__dict__ == {'a': 100, 'b': 1, 'c': 200}
# obj3.display()
# class Point:
#     def set_coordinates(self, x, y):
#         self.x = x
#         self.y = y
#
#     def get_distance(self, obj):
#         if hasattr(Point, 'obj'):
#             r = ((self.x - obj.x) ** 2 + (self.y - obj.y) ** 2) ** 0.5
#             return r
#         else:
#             print('Передана не точка')
#
#         # Код ниже не удаляйте, он нужен для проверок


#
# p1 = Point()
# p2 = Point()
# assert isinstance(p1, Point)
# assert isinstance(p2, Point)
#
# p1.set_coordinates(1, 2)
# assert p1.x == 1
# assert p1.y == 2
# p2.set_coordinates(4, 6)
# assert p2.x == 4
# assert p2.y == 6
# assert p1.get_distance(p2) == 5.0
# p3 = Point()
# p3.set_coordinates(10, 10)
# p1.set_coordinates(4, 2)
# assert p1.get_distance(p3) == 10.0
# res = p1.get_distance(10)  # Распечатает "Передана не точка", вернет None
# assert res is None, 'Метод get_distance должен возвращать None, если в него была передана не точка'
#
# assert p2.get_distance([1, 2, 3]) is None  # Распечатает "Передана не точка", вернет None

#
# class Hero():
#
#     def __init__(self, name, posessions):
#         self.name = name
#         self.posessions = posessions
#
#     def __repr__(self):
#         return f'Герой {hero.name} взял с собой {", ".join(hero.posessions)}'
#
#
# # Не удаляйте код ниже, он нужен для проверки
#
# hero = Hero("Питомир", ["меч", "плащ", "шляпа"])
# print(hero)
# Напишите определение класса SoccerPlayer
# class Zebra:
#     def __init__(self,color):
#         self.color1 = 'Полоска белая'
#         self.color2 = 'Полоска черная'
#
#     def which_stripe(self):
#         print(self.color1)
#         self.color1, self.color2 = self.color2, self.color1
#
#
# z1 = Zebra()
# print(z1.which_stripe())


# class Person:
#     def __init__(self, first_name, last_name, age):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#
#     def full_name(self):
#         full_name = f'{self.last_name} {self.first_name}'
#         return full_name
#
#     def is_adult(self):
#         if self.age >= 18:
#             return True
#         return False
#
#
# # Ниже код для проверки методов класса Person
# p1 = Person('Ash', 'Ketchum', 20)
# assert isinstance(p1, Person)
# assert p1.full_name() == 'Ketchum Ash'
# assert p1.age == 20
# assert p1.first_name == 'Ash'
# assert p1.last_name == 'Ketchum'
# assert p1.is_adult() is True
#
# p2 = Person('Hermione', 'Granger', 16)
# assert isinstance(p2, Person)
# assert p2.age == 16
# assert p2.first_name == 'Hermione'
# assert p2.last_name == 'Granger'
# assert p2.full_name() == 'Granger Hermione'
# assert p2.is_adult() is False
# print('Good')
# Напишите определение класса Stack
# class Stack:
#     def __init__(self):
#         self.values = []
#
#     def push(self, item):
#         self.values.append(item)
#
#     def pop(self):
#         if self.values:
#             return self.values.pop()
#         print('Empty Stack')
#
#     def peek(self):
#         if self.values:
#             return self.values[-1]
#         print('Empty Stack')
#
#     def is_empty(self):
#         return not self.values
#
#     def size(self):
#         return len(self.values)
#
#
# # Ниже код для проверки класса Stack
#
# s = Stack()
# assert s.values == []
# assert isinstance(s, Stack)
#
# s.peek()  # распечатает 'Empty Stack'
# assert s.is_empty() is True
# s.push('cat')
# assert s.size() == 1
# assert s.peek() == 'cat'
#
# s.push('dog')
# assert s.size() == 2
# assert s.peek() == 'dog'
#
# s.push(True)
# assert s.size() == 3
# assert s.is_empty() is False
#
# s.push(777)
# assert s.size() == 4
#
# assert s.pop() == 777
# assert s.size() == 3
#
# assert s.pop() is True
# assert s.size() == 2
#
# s.push(123)
# s.push(123456)
# assert s.peek() == 123456
# assert s.size() == 4
#
# assert s.pop() == 123456
# assert s.pop() == 123
# assert s.pop() == 'dog'
# assert s.is_empty() is False
# assert s.pop() == 'cat'
# assert s.is_empty() is True
#
# d = Stack()
# assert d.peek() is None  # Печатает "Empty Stack"
# assert d.pop() is None  # Печатает "Empty Stack"
# d.push('hello')
# assert d.size() == 1
# d.push('world')
# assert d.size() == 2
# assert d.peek() == 'world'
# assert d.pop() == 'world'
# assert d.peek() == 'hello'
# lst = [1]
# for i in range(2,5):
#     if lst:
#         lst.append(i)
#         print(lst)
# persons = [
#     ('Allison Hill', 334053, 'M', '1635644202'),
#     ('Megan Mcclain', 191161, 'F', '2101101595'),
#     ('Brandon Hall', 731262, 'M', '6054749119'),
#     ('Michelle Miles', 539898, 'M', '1355368461'),
#     ('Donald Booth', 895667, 'M', '7736670978'),
#     ('Gina Moore', 900581, 'F', '7018476624'),
#     ('James Howard', 460663, 'F', '5461900982'),
#     ('Monica Herrera', 496922, 'M', '2955495768'),
#     ('Sandra Montgomery', 479201, 'M', '5111859731'),
#     ('Amber Perez', 403445, 'M', '0602870126')
# ]
#
#
# class Worker:
#     def __init__(self, name, salary, gender, passport):
#         self.name = name
#         self.salary = salary
#         self.gender = gender
#         self.passport = passport
#
#     def get_info(self):
#         return f'Worker {self.name};passport - {self.passport}'
#
#
# worker_objects = []
#
# for i, per in enumerate(persons):
#     name, salary, gender, passport = per
#     worker_objects.append(Worker(name, salary, gender, passport))
# for i in worker_objects:
#     print(i.get_info())
# class CustomLabel:
#     def __init__(self, text, **kw):
#         self.text = text
#         for key, value in kw.items():
#             self.__dict__[key] = value
#
#     def config(self, **kw):
#         return self.__dict__.update(kw)
#
# # Ниже код для проверки методов класса CustomLabel
# label1 = CustomLabel(text="Hello Python", fg="#eee", bg="#333")
# label2 = CustomLabel(text="Username")
# label3 = CustomLabel(text="Password", font=("Comic Sans MS", 24, "bold"), bd=20, bg='#ffaaaa')
# label4 = CustomLabel(text="Hello", bd=20, bg='#ffaaaa')
# label5 = CustomLabel(text="qwwerty", a=20, b='#ffaaaa', r=[3, 4, 5, 6], p=32)
#
# assert label1.__dict__ == {'text': 'Hello Python', 'fg': '#eee', 'bg': '#333'}
# assert label2.__dict__ == {'text': 'Username'}
# assert label3.__dict__ == {'text': 'Password', 'font': ('Comic Sans MS', 24, 'bold'), 'bd': 20, 'bg': '#ffaaaa'}
# assert label4.__dict__ == {'text': 'Hello', 'bd': 20, 'bg': '#ffaaaa'}
# assert label5.__dict__ == {'text': 'qwwerty', 'a': 20, 'b': '#ffaaaa', 'r': [3, 4, 5, 6], 'p': 32}
#
# print(label1.__dict__)
# print(label2.__dict__)
# print(label3.__dict__)
# print(label4.__dict__)
# print(label5.__dict__)
#
# label4.config(color='red', bd=100)
# label5.config(color='red', bd=100, a=32, b=432, p=100, z=432)
#
# assert label4.__dict__ == {'text': 'Hello', 'bd': 100, 'bg': '#ffaaaa', 'color': 'red'}
# assert label5.__dict__ == {'text': 'qwwerty', 'a': 32, 'b': 432, 'r': [3, 4, 5, 6], 'p': 100,
#                            'color': 'red', 'bd': 100, 'z': 432}

# class Player:
#     def __init__(self, name):
#         self.name = name
#         self.choice = None
#
# t = Player('ds')
# print(t.choice)
# Напишите определение классов Person, Company и Employee
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def display_person_info(self):
#         print(f'Person {self.name}, {self.age}')
#
#
# class Company:
#     def __init__(self, company_name, location):
#         self.company_name = company_name
#         self.location = location
#
#     def display_company_info(self):
#         print(f'Company {self.company_name}, {self.location}')
#
#
# class Employee:
#     def __init__(self):
#         self.personal_data = Person(name, age)
#         self.work = Company(company_name, location)

# Напишите определение классов Task, TaskList и TaskManager
# class Task:
#     def __init__(self, name, description, status=False):
#         self.name = name
#         self.description = description
#         self.status = status
#
#     def display(self):
#         if self.status:
#             print(f'{self.name} (Сделана)')
#         else:
#             print(f'{self.name} (Не сделана)')
#
#
# class TaskList:
#     def __init__(self):
#         self.tasks = []
#
#     def add_task(self, task):
#         self.tasks.append(task)
#
#     def remove_task(self, task):
#         self.tasks.remove(task)
#
#
# class TaskManager:
#     def __init__(self,):
#         self.task_list = TaskList()
#
#     def mark_done(self,task):
#         self.task = task
#         task.status = False
#
#     def mark_undone(self,task):
#         self.task = task
#         task.status = False
#
#     def show_tasks(self):
#         for task in self.task_list.tasks:
#             Task.display(task)
# class AAA:
#     def __int__(kosheka):
#         kosheka.name = 'Python'
# class Constructor:
#     def add_atribute(self, name, value):
#         setattr(self, 'name', value)
#
#     def display(self):
#         print(self.__dict__)
# class Zebra:
#     def __init__(self):
#         self.stripe = True
#
#     def which_stripe(self):
#         print('Полоска белая' if self.stripe else 'Полоска черная')
#         self.stripe = not self.stripe
#
#
# t = Zebra()
# persons = [
#     ('Allison Hill', 334053, 'M', '1635644202'),
#     ('Megan Mcclain', 191161, 'F', '2101101595'),
#     ('Brandon Hall', 731262, 'M', '6054749119'),
#     ('Michelle Miles', 539898, 'M', '1355368461'),
#     ('Donald Booth', 895667, 'M', '7736670978'),
#     ('Gina Moore', 900581, 'F', '7018476624'),
#     ('James Howard', 460663, 'F', '5461900982'),
#     ('Monica Herrera', 496922, 'M', '2955495768'),
#     ('Sandra Montgomery', 479201, 'M', '5111859731'),
#     ('Amber Perez', 403445, 'M', '0602870126')
# ]
#
#
# class Worker:
#     def __init__(self, name, salary, gender, passport):
#         self.name = name
#         self.salary = salary
#         self.gender = gender
#         self.passport = passport
#         self.get_info()
#
#     def get_info(self):
#         print(f'Worker {self.name};passport - {self.passport}')
#
#
# worker_objects = []
#
# for per in persons:
#     worker_objects.append(Worker(*per))
# persons = [
#     ('Allison Hill', 334053, 'M', '1635644202'),
#     ('Megan Mcclain', 191161, 'F', '2101101595'),
#     ('Brandon Hall', 731262, 'M', '6054749119'),
#     ('Michelle Miles', 539898, 'M', '1355368461'),
#     ('Donald Booth', 895667, 'M', '7736670978'),
#     ('Gina Moore', 900581, 'F', '7018476624'),
#     ('James Howard', 460663, 'F', '5461900982'),
#     ('Monica Herrera', 496922, 'M', '2955495768'),
#     ('Sandra Montgomery', 479201, 'M', '5111859731'),
#     ('Amber Perez', 403445, 'M', '0602870126')
# ]
#
#
# class Worker:
#     def __init__(self, name, salary, gender, passport):
#         self.name = name
#         self.salary = salary
#         self.gender = gender
#         self.passport = passport
#         self.get_info()
#
#     def get_info(self):
#         print(f'Worker {self.name}; passport-{self.passport}')
#
#
# worker_objects = []
# for worker in persons:
#     worker_objects.append(Worker(*worker))
# class CustomLabel:
#     def __int__(self, text, **kwargs):
#         self.text = text
#         self.args = kwargs
#
#     def config(self, **kwargs):
#         setattr(self, kwargs)
#  напишите определение класса WeatherStation
# class WeatherStation:
#     __shared_attr = {
#         'temperature': 0,
#         'humidity': 0,
#         'pressure': 0
#     }
#
#     def __init__(self):
#         self.__dict__ = WeatherStation.__shared_attr
#
#     def update_data(self, temperature, humidity, pressure):
#         self.temperature = temperature
#         self.humidity = humidity
#         self.pressure = pressure
#
#     def get_current_data(self):
#         return self.temperature, self.humidity, self.pressure
#
#
# # код для проверки
# sensor1 = WeatherStation()
# assert sensor1.temperature == 0
# assert sensor1.humidity == 0
# assert sensor1.pressure == 0
# sensor2 = WeatherStation()
# assert sensor2.get_current_data() == (0, 0, 0)
# sensor1.update_data(25, 60, 103)
# assert sensor1.get_current_data() == (25, 60, 103)
# print(sensor2.get_current_data())
# assert sensor2.get_current_data() == (25, 60, 103)
# sensor3 = WeatherStation()
# assert sensor3.get_current_data() == (25, 60, 103)
# sensor3.update_data(50, 20, 10)
# assert sensor1.get_current_data() == (50, 20, 10)
# assert sensor2.get_current_data() == (50, 20, 10)
# print('Good')

# print(load_random_word(lst_of_words))
#
#
# def get_subwords(lst_words):
#     subwords = []
#     for word in lst_words:
#         subwords.append(word['subwords'])
#     return subwords
#
# print(get_subwords(lst_of_words))
#
# class AverageCalculator:
#     def __init__(self, numbers):
#         self.numbers = numbers
#
#     def __calculate_average(self):
#         total = sum(self.numbers)
#         return total / len(self.numbers)
#
#
# average_calculator = AverageCalculator([1, 2, 3])
# print(dir(average_calculator))
# print(average_calculator._AverageCalculator__calculate_average())
# class PizzaMaker:
#     def __make_pepperoni(self):
#         pass
#
#     def _make_barbecue(self):
#         pass
#
# maker = PizzaMaker()
# print(PizzaMaker.__dict__.keys())
# print(maker._make_barbecue())
# print(maker._PizzaMaker__make_pepperoni())
# class Student:
#     def __init__(self,
#
#                  __name, __age, __branch):
#         self.__name = __name
#         self.__age = __age
#         self.__branch = __branch
#
#     def __display_details(self):
#         print(f'Имя: {self.__name}\n'
#               f'Возраст: {self.__age}\n'
#               f'Направление: {self.__branch}')
#
#     def access_private_method(self):
#         return self.__display_details()
#
#
# obj = Student("Adam Smith", 25, "Information Technology")
# obj.access_private_method()
# Напишите определение класса BankDeposit
# class BankDeposit:
#     def __init__(self, name, balance, rate):
#         self.name = name
#         self.balance = balance
#         self.rate = rate
#
#     def __calculate_profit(self):
#         return (self.balance / 100) * self.rate
#
#     def get_balance_with_profit(self):
#         return self.balance + (self.balance / 100) * self.rate
#
#
# # Ниже код для проверки методов класса BankDeposit
# account = BankDeposit("John Connor", 1000, 5)
# assert account.name == "John Connor"
# assert account.balance == 1000
# assert account.rate == 5
# assert account._BankDeposit__calculate_profit() == 50.0
# print(account.get_balance_with_profit())
# assert account.get_balance_with_profit() == 1050.0
#
# account_2 = BankDeposit("Sarah Connor", 200, 27)
# assert account_2.name == "Sarah Connor"
# assert account_2.balance == 200
# assert account_2.rate == 27
# assert account_2._BankDeposit__calculate_profit() == 54.0
# assert account_2.get_balance_with_profit() == 254.0
# print('Good')


# Ниже код для проверки методов класса Library
# Напишите определение класса Library
# class Library:
#     def __init__(self, __books):
#         self.__books = __books
#
#     def __check_availability(self, book):
#         return book in self.__books
#
#     def search_book(self, book):
#         return self.__check_availability(book)
#
#     def return_book(self, book):
#         self.__books.append(book)
#
#     def _checkout_book(self, name_book):
#         if name_book in self.__books:
#             self.__books.remove(name_book)
#             return True
#         return False
#
#
# # Ниже код для проверки методов класса Library
# library = Library(["War and Peace", "Moby-Dick", "Pride and Prejudice"])
#
# assert library._Library__books == ["War and Peace", "Moby-Dick", "Pride and Prejudice"]
# assert library.search_book("Moby-Dick") == True
# assert library.search_book("Jane Air") == False
#
# assert library._Library__check_availability("War and Peace") == True
# assert library._checkout_book("Moby-Dick") == True
# assert library._Library__books == ["War and Peace", "Pride and Prejudice"]
#
# assert library.search_book("Moby-Dick") == False
# assert library.return_book("Moby-Dick") is None
# assert library._Library__books == ["War and Peace", "Pride and Prejudice", "Moby-Dick"]
# assert library.search_book("Moby-Dick") == True
# print('Good')
# Напишите определение класса Employee
# class Employee:
#     def __init__(self, name, __position, __hours_worked, __hourly_rate):
#         self.name = name
#         self.__position = __position
#         self.__hours_worked = __hours_worked
#         self.__hourly_rate = __hourly_rate
#
#     def __calculate_salary(self):
#         return self.__hours_worked * self.__hourly_rate
#
#     def _set_position(self, new_position):
#         self.__position = new_position
#
#     def get_position(self):
#         return self.__position
#
#     def get_salary(self):
#         return self.__calculate_salary()
#
#     def get_employee_details(self):
#         return f"Name: {self.name}, Position: {self.__position}, Salary: {self.__calculate_salary()}"
# # Ниже код для проверки методов класса Employee
# employee = Employee("Джеки Чан", 'manager', 20, 40)
# assert employee.name == 'Джеки Чан'
# assert employee._Employee__hours_worked == 20
# assert employee._Employee__hourly_rate == 40
# assert employee._Employee__position == 'manager'
# assert employee.get_position() == 'manager'
# assert employee.get_salary() == 800
# assert employee._Employee__calculate_salary() == 800
# assert employee.get_employee_details() == 'Name: Джеки Чан, Position: manager, Salary: 800'
# employee._set_position('Director')
# assert employee.get_employee_details() == 'Name: Джеки Чан, Position: Director, Salary: 800'
#
# employee_2 = Employee("Пирс Броснан", 'actor', 35, 30)
# assert employee_2._Employee__calculate_salary() == 1050
# assert employee_2.get_employee_details() == 'Name: Пирс Броснан, Position: actor, Salary: 1050'
#
# print('Good')
# def greet(*args):
#     i = 'Hello'
#     if len(args) > 1:
#
#         return f'{i}, {args} {i}'
#
# # print(greet('sds','ewew'))
# def greet(name, *args):
#     return f'Hello,{" and ".join((name,)+ args)}'
#
# print(greet('sdsd','sdsd'))
# Напишите определение класса Employee
# new_email = 'hello@.w3'
# print(new_email.index('@.'))
# Напишите определение класса UserMail
# class UserMail:
#     def __init__(self, login, email):
#         self.login = login
#         self.__email = email
#
#     def get_email(self):
#         return self.__email
#
#     def set_email(self, new_email):
#         if str(new_email).count('@') == 1 and new_email.count('.')
#         == 1 and new_email.index('@') < new_email.index('.'):
#             self.__email = new_email
#         else:
#             print(f'ErrorMail:{new_email}')
#
#     email = property(fget=get_email, fset=set_email)
# # Ниже код для проверки методов класса UserMail
#
# jim = UserMail("aka47", 'hello@com.org')
# assert jim.login == "aka47"
# assert jim._UserMail__email == "hello@com.org"
# assert isinstance(jim, UserMail)
# assert isinstance(type(jim).email, property), 'Вы не создали property email'
#
# jim.email = [1, 2, 3]  # печатает ErrorMail:[1, 2, 3]
# jim.email = 'hello@@re.ee'  # печатает ErrorMail:hello@@re.ee
# jim.email = 'hello@re.w3'
# assert jim.email == 'hello@re.w3'
#
# k = UserMail('belosnezhka', 'prince@wait.you')
# assert k.email == 'prince@wait.you'
# assert k.login == 'belosnezhka'
# assert isinstance(k, UserMail)
#
# k.email = {1, 2, 3}  # печатает ErrorMail:{1, 2, 3}
# k.email = 'prince@still@.wait'  # печатает ErrorMail:prince@still@.wait
# k.email = 'prince@stillwait'  # печатает ErrorMail:prince@stillwait
# k.email = 'prince@still.wait'
# assert k.get_email() == 'prince@still.wait'
# k.email = 'pri.nce@stillwait'  # печатает ErrorMail:pri.nce@stillwait
# assert k.email == 'prince@still.wait'
# def text_decor(func):
#     def inner(*args, **kwargs):
#         print('Hello')
#         func(*args, **kwargs)
#         print('Goodbye!')
#
#     return inner
#
#
#
# @text_decor
# def just_func():
#     print('I just simple python func')
#
#
# print(just_func())
#
#
# def func():
#     def inner(s):
#         return '<h1>' + s + '</h1>'
#
#     return inner
#
#
# res = func()
# print(res('sds'))
# def outer(symbol):
#     def inner(str):
#         return symbol + str + symbol
#
#     return inner
# def create_dict():
#     def inner(value):
#         key = 0
#         my_dict = {key + 1: value}
#         return my_dict
#
#     return inner
# print(create_dict()('ede'))
# print(create_dict()(400))
# print(create_dict()(400))
# from math import floor
# if 4 > 3:
#     print('dd')
# if 4 > 2:
#     print('see')
# put your python code here
# text = input()
# for i in text:
#     if i in 'а, у, о, ы, и, э, я, ю, ё, е':
#         print('sd')
# put your python code here
# text = input()
# lst_gl = []
# lst_sg = []
# for i in text:
#     if i in 'ауоыиэяюёе':
#         lst_gl.append(i)
#     elif i in 'бвгджзйклмнпрстфхцчшщ':
#         lst_sg.append(i)
# print(f'Количество гласных букв равно {len(lst_gl)}\nКоличество согласных букв равно {len(lst_sg)}')
# text = input().capitalize()
# lst = []
# for i in text:
#     if i.isdigit():
#         lst.append(i)
# numbers = set(lst)
# print(*sorted(list(numbers)) if len(numbers) > 0 else 'НЕТ')
# def strip_string(string, strip_chars=' '):
#     return string.strip(strip_chars)
#
#
# print(strip_string('   dsds   '))
# print(strip_string('  wewe  '))
# def counter_add():
#     def inner(n):
#         return n + 5
#
#     return inner
#
#
# k = int(input())
# # cnt = counter_add()
# print(counter_add()(k))
# def get_sq(width, height):
#     return width * height
#
#
# def func_show(func):
#     def inner(*args, **kwargs):
#         return f'Площадь прямоугольника: {func(*args, **kwargs)}'
#
#     return inner
#
#
# widt, heigh = list(map(int, input().split()))
# get_sq = func_show(get_sq)
# print(get_sq(widt, heigh))
#
#
# def get_sq(width, height):
#     return f'Площадь прямоугольника: {width * height}'
#
#
# def func_show(func):
#     def inner(*args, **kwargs):
#         return func(*args, **kwargs)
#
#     return inner
#
#
# width, height = map(int, input().split())
# get_sq = func_show(get_sq)
# print(get_sq(width, height))
# s = input()
#
#
# def show_menu(func):
#     def inner(*args, **kwargs):
#         return func(args)
#
#     return inner
#
#
# @show_menu
# def get_menu(s):
#     return list(s)
#
#
# print(show_menu(get_menu))
# put your python code here
# text = input().split()
#
#
# def outer(func):
#     def inner(*args):
#         lst_numbers = func(*args)
#         return sorted(lst_numbers)
#
#     return inner
#
#
# @outer
# def get_list(numbers):
#     num = [int(i) for i in numbers if i.isdigit()]
#     return num
#
#
# lst = get_list(text)
# print(*lst)
# put your python code here
# def outer(func):
#     def inner(*args):
#         d = zip(func(*args))
#
#     return inner
#
#
# @outer
# def func(s1, s2):
#     return s1.split(), s2.split()


# t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
#      'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
#      'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
#      'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}
#
# # здесь продолжайте программу
# s = input().lower()


# Python - это круто!
#
# def outer(func):
#     def inner(*args):
#         text = func(*args)
#         while "--" in text:
#             text = text.replace('--', '-')
#         return text
#
#     return inner
#
#
# @outer
# def change_text(text):
#     lst = []
#     for i in text:
#         if i in t:
#             lst.append(t[i])
#         elif i in '.,;: ':
#             i = '-'
#             lst.append(i)
#         else:
#             lst.append(i)
#     return ''.join(lst)
#
#
# change_text = outer(change_text)(s)
# print(change_text)
# from functools import wraps
#
#
# # Напишите определение декоратора add_args
# def add_args(func):
#     @wraps(func)
#     def inner(*args, **kwargs):
#         text = func(*args,**kwargs).split()
#         text.insert(0,'begin')
#         text.append('end')
#         return f'{" ".join(text)}'
#
#     return inner
#
#
# # Код ниже не удаляйте, он нужен для проверки
# @add_args
# def concatenate(*args):
#     """
#     Возвращает конкатенацию переданных строк
#     """
#     return ', '.join(args)
#
#
# @add_args
# def find_max_word(*args):
#     """
#     Возвращает слово максимальной длины
#     """
#     return max(args, key=len)
#
#
# print(concatenate('hello', 'world', 'my', 'name is', 'Artem'))
# # assert concatenate('hello', 'world', 'my', 'name is', 'Artem') == 'begin, hello, world, my, name is, Artem, end'
# # assert concatenate('my', 'name is', 'Artem') == 'begin, my, name is, Artem, end'
# # assert concatenate.__name__ == 'concatenate'
# # assert concatenate.__doc__.strip() == """Возвращает конкатенацию переданных строк"""
# print(find_max_word('my'))
# assert find_max_word('my') == 'begin'
# assert find_max_word('my', 'how') == 'begin'
# assert find_max_word('my', 'how', 'maximum') == 'maximum'
# assert find_max_word.__name__ == 'find_max_word'
# assert find_max_word.__doc__.strip() == """Возвращает слово максимальной длины"""
# from functools import wraps
#
#
# # Напишите определение декоратора validate_args
# def validate_args(func):
#     @wraps(func)
#     def inner(*args):
#         if len(args) < 2:
#             return f'Not enough arguments'
#         elif len(args) > 2:
#             return f'Too many arguments'
#         elif not isinstance(args[0], int) or type(args[1]) != int:
#             return f'Wrong types'
#         else:
#             return func(*args)
#     return inner
#
#
# # Код ниже не удаляйте, он нужен для проверки
# @validate_args
# def add_numbers(x, y):
#     """Return sum of x and y"""
#     return x + y


# assert add_numbers(4, 5) == 9
# assert add_numbers(4) == 'Not enough arguments'
# assert add_numbers() == 'Not enough arguments'
# assert add_numbers('hello') == 'Not enough arguments'
# assert add_numbers(3, 5, 6) == 'Too many arguments'
# assert add_numbers('a', 'b', 'c') == 'Too many arguments'
# assert add_numbers(4.5, 5.1) == 'Wrong types'
# assert add_numbers('hello', 4) == 'Wrong types'
# assert add_numbers(9, 'hello') == 'Wrong types'
# assert add_numbers([1, 3], {}) == 'Wrong types'
# assert add_numbers.__name__ == 'add_numbers'
# assert add_numbers.__doc__.strip() == 'Return sum of x and y'
# print('Good')
s = input()


def show_menu(func):
    def inner(*args):
        menu = func(*args)
        for i, word in enumerate(menu, start=1):
            print(f'{i}. {word}')

    return inner

@show_menu
def get_menu(s):
    return list(s.split())


get_menu(s)