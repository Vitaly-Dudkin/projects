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
# r = Library('sds')
# print(Library.return_book('sd','dssd'))
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
# s = input()
#
#
# def show_menu(func):
#     def inner(*args):
#         menu = func(*args)
#         for i, word in enumerate(menu, start=1):
#             print(f'{i}. {word}')
#
#     return inner
#
# @show_menu
# def get_menu(s):
#     return list(s.split())
#
#
# get_menu(s)
# class Notebook:
#     def __init__(self, _notes):
#         self._notes = _notes
#
#     @property
#     def notes_list(self):
#         for i, word in enumerate(self._notes):
#             print(f'{i}.{word}')
#
#
# note = Notebook(['Buy Potato', 'Buy Carrot', 'Wash car'])
# note.notes_list
# class Square:
#     def __init__(self, side):
#         self.side = side
#
#     @property
#     def side(self):
#         return self._side
#
#     @side.setter
#     def side(self, value):
#         self._side = float(value)
#
#     @property
#     def area(self):
#         return self.side ** 2
#
#     @area.setter
#     def area(self, value):
#         self.side = value ** 0.5
#
#
#
# r = Square(5)
# r.area = 45
# print(r.area)
# class Money:
#     def __init__(self, dollars, cents):
#         self.dollars = dollars
#         self.cents = cents
#         self.total_cents = self.dollars * 100 + self.cents
#
#     @property
#     def dollars(self):
#         return self.dollars
#
#     @dollars.setter
#     def dollars(self, value):
#         if isinstance(value, int) and value >= 0:
#             self.total_cents = value * 100
#             return self.total_cents
#         return "Error dollars"
#
#     @property
#     def cents(self):
#         return self.cents
#
#     @cents.setter
#     def cents(self, value):
#         if isinstance(value, (int, float)) and value < 100:
#             self.cents = value
#             return self.cents
#         return "Error cents"
#
#     def __str__(self):
#         return f"Ваше состояние составляет {self.dollars} долларов {self.cents} центов"
#
#
# Bill = Money(101, 99)
# Напишите определение класса Rectangle
# class Rectangle:
#     def __init__(self, widt, height):
#         self.widt = widt
#         self.height = height
#         self.__area = None
#
#     @property
#     def area(self):
#         if self.__area == None:
#             return self.height * self.widt
#         return self.area
#
#
# # Ниже код для проверки методов класса Rectangle
#
#
# r1 = Rectangle(5, 10)
# assert isinstance(r1, Rectangle)
# assert r1.area == 50
# assert isinstance(type(r1).area, property), 'Вы не создали property area'
#
# r2 = Rectangle(15, 3)
# assert isinstance(r2, Rectangle)
# assert r2.area == 45
# assert isinstance(type(r2).area, property), 'Вы не создали property area'
#
# r3 = Rectangle(43, 232)
# assert r3.area == 9976
# print('Good')
# class Car:
#
#     def __init__(self, model, color):
#         self.model = model
#         self.color = color
#
#     @classmethod
#     def get_red_car(cls, model):
#         return cls(model, 'res')
#
#
# car1 = Car.get_red_car('Audi')
# print(car1, car1.model, car1.color)
#
# car2 = Car.get_red_car('BMW')
# print(car2, car2.model, car2.color)
# class Robot:
#     population = 0
#
#     def __init__(self, name):
#         self.name = name
#         print(f'Робот {self.name} был создан')
#         Robot.population += 1
#
#     def destroy(self):
#         Robot.population -= 1
#         print("Робот {name} был уничтожен")
#
#     def say_hello(self):
#         print(f"Робот {self.name} приветствует тебя, особь человеческого рода")
#
#     @classmethod
#     def how_many(cls):
#         print(f"{cls.population}, вот сколько нас еще осталось")
#
#
# # код ниже не нужно удалять, в нем находятся проверки
#
# droid1 = Robot("R2-D2")
# assert droid1.name == 'R2-D2'
# assert Robot.population == 1
# droid1.say_hello()
# Robot.how_many()
# droid2 = Robot("C-3PO")
# assert droid2.name == 'C-3PO'
# assert Robot.population == 2
# droid2.say_hello()
# Robot.how_many()
# droid1.destroy()
# assert Robot.population == 1
# droid2.destroy()
# assert Robot.population == 0
# Robot.how_many()
# class User:
#     def __init__(self, name, role):
#         self.name = name
#         self.role = role
#
#
# class Access:
#     __access_list = ['admin', 'developer']
#
#     @staticmethod
#     def __check_access(role):
#         return role in Access.__access_list
#
#     @staticmethod
#     def get_access(user_obj):
#         if isinstance(user_obj, User) and Access.__check_access:
#             print(f'User {user_obj.name}: success')
#         elif not isinstance(user_obj, User):
#             print('AccessTypeError')
#         elif not Access.__check_access:
#             print('AccessDenied')
#
#
# r = User('vit','admin')
# Access.get_access(
# from string import digits
# import string
#
# forbidden = ['123456', 'password', '123456789', '12345', '12345678', 'qwerty', '1234567', '111111', '1234567890',
#              '123123', 'abc123', '1234', 'password1', 'iloveyou', '1q2w3e4r', '000000', 'qwerty123', 'zaq12wsx',
#              'dragon', 'sunshine', 'princess', 'letmein', '654321', 'QwerTy123', 'KissasSAd1f', 'monkey', '27653',
#              '1qaz2wsx', '123321', 'qwertyuiop', 'superman', 'asdfghjkl']
#
#
# class Registration:
#     def __init__(self, логин, пароль):
#         self.login = логин
#         self.password = пароль
#
#     @property
#     def login(self):
#         return self.__login
#
#     @property
#     def password(self):
#         return self.__password
#
#     @staticmethod
#     def is_include_digit(password):
#         for digit in digits:
#             if digit in password:
#                 return True
#         return False
#
#     @staticmethod
#     def is_include_only_latin(password):
#         for i in password:
#             if i.isalpha():
#                 if i not in string.ascii_letters:
#                     return True
#         return False
#
#     @staticmethod
#     def is_include_all_register(password):
#         return all([bool(set(password) & set(string.ascii_uppercase)),
#                     bool(set(password) & set(string.ascii_lowercase))])
#
#     @password.setter
#     def password(self, password):
#         if not isinstance(password, str):
#             raise TypeError("Пароль должен быть строкой")
#         elif 5 > len(password) or 11 < len(password):
#             raise ValueError('Пароль должен быть длиннее 4 и меньше 12 символов')
#         elif not Registration.is_include_digit(password):
#             raise ValueError('Пароль должен содержать хотя бы одну цифру')
#         elif not Registration.is_include_all_register(password):
#             raise ValueError('Пароль должен содержать хотя бы один символ верхнего и нижнего регистра')
#         elif Registration.is_include_only_latin(password):
#             raise ValueError('Пароль должен содержать только латинский алфавит')
#         elif password in forbidden:
#             raise ValueError('Ваш пароль содержится в списке самых легких')
#         else:
#             self.__password = password
#
#     @login.setter
#     def login(self, login):
#         if not isinstance(login, str):
#             raise TypeError
#         if login.index('@') > login.index('.'):
#             raise ValueError
#         else:
#             self.__login = login
#

# r1 = Registration('qwerty@rambler.ru', 'QwrRt124')  # здесь хороший логин
# print(r1.login, r1.password)  # qwerty@rambler.ru QwrRt124
# # теперь пытаемся запись плохие пароли
# # r1.password = '123456'  # ValueError('Пароль должен содержать хотя бы один символ верхнего и нижнего регистра')
# # r1.password = 'LoW'  # raise ValueError('Пароль должен быть длиннее 4 и меньше 12 символов')
# # r1.password = 43  # raise TypeError("Пароль должен быть строкой")
# r1.password = 'dcQ1dQ'
# print(r1.password)
# from string import digits
# import string
#
# forbidden = ['123456', 'password', '123456789', '12345', '12345678', 'qwerty', '1234567', '111111', '1234567890',
#              '123123', 'abc123', '1234', 'password1', 'iloveyou', '1q2w3e4r', '000000', 'qwerty123', 'zaq12wsx',
#              'dragon', 'sunshine', 'princess', 'letmein', '654321', 'QwerTy123', 'KissasSAd1f', 'monkey', '27653',
#              '1qaz2wsx', '123321', 'qwertyuiop', 'superman', 'asdfghjkl']
#
#
# class Registration:
#     def __init__(self, логин, пароль):
#         self.login = логин
#         self.password = пароль
#
#     @property
#     def login(self):
#         return self.__login
#
#     @property
#     def password(self):
#         return self.__password
#
#     @staticmethod
#     def is_include_digit(password):
#         for i in password:
#             if i in digits:
#                 return True
#             return False
#
#     @staticmethod
#     def is_include_only_latin(password):
#         for i in password:
#             if i not in string.ascii_letters:
#                 return True
#             return False
#
#     @staticmethod
#     def is_include_all_register(password):
#         for i in password:
#             if i in string.ascii_uppercase:
#                 return True
#             return False
#
#     @password.setter
#     def password(self, password):
#         if not isinstance(password, str):
#             raise TypeError("Пароль должен быть строкой")
#         elif 5 > len(password) or 11 < len(password):
#             raise ValueError('Пароль должен быть длиннее 4 и меньше 12 символов')
#         elif Registration.is_include_digit(password):
#             raise ValueError('Пароль должен содержать хотя бы одну цифру')
#         elif Registration.is_include_all_register(password):
#             raise ValueError('Пароль должен содержать хотя бы один символ верхнего и нижнего регистра')
#         elif Registration.is_include_only_latin(password):
#             raise ValueError('Пароль должен содержать только латинский алфавит')
#         elif password in forbidden:
#             raise ValueError('Ваш пароль содержится в списке самых легких')
#         else:
#             self.__password = password
#
#     @login.setter
#     def login(self, login):
#         if not isinstance(login, str):
#             raise TypeError
#         if login.index('@') > login.index('.'):
#             raise ValueError
#         else:
#             self.__login = login
# Напишите определение классов File и Trash
# class File:
#     def __init__(self, name):
#         self.name = name
#         self.in_trash = False
#         self.is_deleted = False
#
#     def restore_from_trash(self):
#         print(f'Файл {self.name} восстановлен из корзины')
#         self.in_trash = False
#
#     def remove(self):
#         print(f'Файл {self.name} был удален')
#         self.is_deleted = True
#
#     def read(self):
#         if self.is_deleted:
#             print(f'ErrorReadFileDeleted({self.name})')
#
#         elif self.in_trash:
#             print(f'ErrorReadFileTrashed({self.name})')
#             return
#         else:
#             print(f'Прочитали все содержимое файла {self.name}')
#             return
#
#     def write(self, content):
#         if self.is_deleted:
#             print(f'ErrorWriteFileDeleted({self.name})')
#             return
#         elif self.in_trash:
#             print(f'ErrorWriteFileTrashed({self.name})')
#             return
#         else:
#             print(f'Записали значение {content} в файл {self.name}')
#
#
# class Trash:
#     content = []
#
#     @staticmethod
#     def add(file):
#         if isinstance(file, File):
#             setattr(File, 'content', file)
#             file.in_trash = True
#         else:
#             print('В корзину добавлять можно только файл')
#
#     @staticmethod
#     def clear():
#         print('Очищаем корзину')
#         for i in Trash.content:
#             Trash.content.remove(i)
#         print('Корзина пуста')
#
#     @staticmethod
#     def restore():
#         print('Восстанавливаем файлы из корзины')
#         for file in Trash.content:
#             file.restore_from_trash()
#         print('Корзина пуста')
#
#
# f1 = File('puppies.jpg')
# f2 = File('cat.jpg')
# f3 = File('xxx.doc')
# passwords = File('pass.txt')
#
# for file in [f1, f2, f3, passwords]:
#     assert file.is_deleted is False
#     assert file.in_trash is False
#
# f3.read()
# f3.remove()
# assert f3.is_deleted is True
# f3.read()
# f3.write('hello')
#
# assert Trash.content == []
#
# Trash.add(f2)
# Trash.add(passwords)
# Trash.add(f3)
#
# f1.read()
# Trash.add(f1)
# f1.read()
#
# for file in [f1, f2, f3, passwords]:
#     assert file.in_trash is True
#
# for f in [f2, passwords, f3, f1]:
#     assert f in Trash.content
#
# Trash.restore()
# assert Trash.content == [], 'После восстановления корзина должна была очиститься'
#
# Trash.add(passwords)
# Trash.add(f2)
# Trash.add('hello')
# Trash.add(f1)
#
# for f in [passwords, f2, f1]:
#     assert f in Trash.content
#
# Trash.clear()
#
# for file in [passwords, f2, f1]:
#     assert file.is_deleted is True
#
# assert Trash.content == [], 'После удаления файлов корзина должна была очиститься'
#
# f1.read()
# result = {}
# for i in range(1,15):
#     result = result.get(i, i ** 2)
# print(result)
# s = 'orange strawberry barley gooseberry apple apricot barley currant orange melon pomegranate banana ' \
#     'banana orange barley apricot plum grapefruit banana quince strawberry barley grapefruit banana grapes melon ' \
#     'strawberry apricot currant currant gooseberry raspberry apricot currant orange lime quince grapefruit barley ' \
#     'banana melon pomegranate barley banana orange barley apricot plum banana quince lime grapefruit strawberry ' \
#     'gooseberry apple barley apricot currant orange melon pomegranate banana
#     banana orange apricot barley plum banana ' \
#     'grapefruit banana quince currant orange melon pomegranate barley plum banana quince barley lime grapefruit ' \
#     'pomegranate barley'.split()
# res = {}
# for i in set(s):
#     res[i] = s.count(i)
#
# print(sorted(res.v
# class Task:
#
#     def __init__(self, name, description, status=False):
#         self.name = name
#         self.description = description
#         self.status = status
#
#     def display(self):
#         if self.status:
#             print(f'{self.description} Сделана')
#         else:
#             print(f'{self.description} Не сделана')
#
#
# class TaskList:
#
#     def __init__(self, tasks=[]):
#         self.tasks = tasks
#
#     def add_task(self, task):
#         self.tasks.append(task)
#
#     def remove_task(self, task):
#         if task in self.tasks:
#             self.tasks.remove(task)
#
#
# class TaskManager:
#
#     def __init__(self, TaskList):
#         self.task_list = TaskList
#
#     def mark_done(self, task):
#         self.task = task
#         task.status = True
#
#     def mark_undone(self, task):
#         self.task = task
#         task.status = False
#
#     def show_tasks(self):
#         for task in self.task_list.tasks:
#             Task.display(task)
# class Person:
#     def __init__(self, name, surname, gender='male'):
#         self.name = name
#         self.surname = surname
#         self.gender = gender
#
#
#
#     def ede(self, gender):
#         if gender not in ['male', 'female']:
#             self.gender = 'male'
#             print("Не знаю, что вы имели ввиду? Пусть это будет мальчик!")
#         else:
#             self.gender = gender
#
#     def __str__(self):
#         if self.gender == 'male':
#             return f"Гражданин {self.surname} {self.name}"
#         elif self.gender == 'female':
#             return f"Гражданка {self.surname} {self.name}"
#
#
# # Ниже код для проверки методов класса Person
# p1 = Person('Chuck', 'Norris')
# assert p1.name == 'Chuck'
# assert p1.surname == 'Norris'
# assert p1.gender == 'male'
# assert isinstance(p1, Person)
# assert str(p1) == 'Гражданин Norris Chuck'
#
# p2 = Person('Оби-Ван', 'Кеноби', True)  # нужно распечатать предупреждение из условия
# assert str(p2) == 'Гражданин Кеноби Оби-Ван'
# print(p2.__dict__)
# assert p2.__dict__ == {'name': 'Оби-Ван', 'surname': 'Кеноби', 'gender': 'male'}
# assert isinstance(p2, Person)
#
# p3 = Person('Mila', 'Kunis', 'female')
# assert isinstance(p3, Person)
# assert str(p3) == 'Гражданка Kunis Mila'
#
# print(p1)
# print(p2)
# print(p3)
# class Vector:
#     def __init__(self, *args):
#         self.values = []
#         self.args = args
#         for num in self.args:
#             if isinstance(num, int):
#                 self.values.append(num)
#
#     def __str__(self):
#         if not self.values:
#             return f'Пустой вектор'
#         else:
#             return f'Вектор({", ".join([str(i) for i in sorted(set(self.values))])})'
#
#
# # Ниже код для проверки методов класса Vector
#
# v1 = Vector(1, 2, 3)
# assert isinstance(v1, Vector)
# print(v1)
# assert str(v1) == 'Вектор(1, 2, 3)'
#
# v2 = Vector()
# assert isinstance(v2, Vector)
# assert str(v2) == 'Пустой вектор'
#
# v3 = Vector([4, 5], 'hello', 3, -1.5, 1, 2)
# assert isinstance(v3, Vector)
# assert sorted(v3.values) == [1, 2, 3]
# print(v3)
# assert str(v3) == 'Вектор(1, 2, 3)'
#
# v4 = Vector([4, 5], 'hello')
# assert str(v2) == 'Пустой вектор'
# assert v2.values == []
#
# v5 = Vector(1, 2, True)
# assert isinstance(v5, Vector)
# print(v5)
# assert str(v5) == 'Вектор(1, 2)'
#
# print(v1)
# print(v2)
# print(v3)
# print(v4)
# s = 'orange strawberry barley gooseberry apple apricot barley currant orange melon pomegranate
# banana banana orange barley apricot plum grapefruit banana quince strawberry barley grapefruit
# banana grapes melon strawberry apricot currant currant gooseberry raspberry apricot currant orange
# lime quince grapefruit barley banana melon pomegranate barley banana orange barley apricot plum banana
# quince lime grapefruit strawberry gooseberry apple barley apricot currant orange melon pomegranate banana
# banana orange apricot barley plum banana grapefruit banana quince currant orange melon pomegranate barley plum
# banana quince barley lime grapefruit pomegranate barley'
# # res = {s.count(i): i for i in sorted(s.split(),reverse=True)}
# # print(res[max(res)])
#
# r = dict(you=1, we='мы', they='они', us='нам')
# print(r)
# class Hero:
#     def __len__(self):
#         return len(self.__dict__)
#
#     def __str__(self):
#         if len(self.__dict__) == 0:
#             return ''
#         else:
#             answer = ''
#             for key, value in sorted(self.__dict__.items()):
#                 answer += f'{key}: {str(value)}\n'
#             answer = answer.rstrip('\n')
#             return answer
#
#
# # Ниже код для проверки методов класса Hero
# hero = Hero()
# assert len(hero) == 0
# hero.health = 50
# hero.damage = 10
# print(hero.__dict__)
# assert len(hero) == 2
# assert str(hero) == '''damage: 10
# health: 50'''
# hero.weapon = ['sword', ' bow']
# hero.skill = 'Некромант'
# assert str(hero) == '''damage: 10
# health: 50
# skill: Некромант
# weapon: ['sword', ' bow']'''
# print(hero)
#
# villain = Hero()
# assert str(villain) == ''
# assert len(villain) == 0
# villain.level = 15
# villain.skill = 'Боец'
# villain.armor = 25
# assert len(villain) == 3
# assert str(villain) == '''armor: 25
# level: 15
# skill: Боец'''
# print(villain)

#
# class MyPoint:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __add__(self, other):
#         return MyPoint(2 * self.x + other.x, 2 * self.y + other.y)
#
#
# p1 = MyPoint(3, 4)
# p2 = MyPoint(5, 12)
# p3 = MyPoint(5, 12)
# p4 = p1 + p2 + p3
# print(p4.x + p4.y)
# Напишите определение класса Rectangle

# Напишите определение класса Rectangle
# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def __add__(self, other):
#         return Rectangle(self.width + other.width, self.height + other.height)
#
#     def __str__(self):
#         return f'Rectangle({self.width}x{self.height})'
#
#
# r1 = Rectangle(5, 10)
# assert r1.width == 5
# assert r1.height == 10
# print(r1)
#
# r2 = Rectangle(20, 5)
# assert r2.width == 20
# assert r2.height == 5
# print(r2)
#
# r3 = r2 + r1
# assert isinstance(r3, Rectangle)
# assert r3.width == 25
# assert r3.height == 15
# print(r3)
#
#
# class Vector:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __repr__(self):
#         return f"Vector({self.x}, {self.y})"
#
#     def __mul__(self, other):
#         return self.x * other.x + self.y * other.y
#
#
# v1 = Vector(2, 3)
# v2 = Vector(4, 3)
# v3 = v1 * v2
# print(v3)
#
#
# class Order:
#     def __init__(self, cart=None, customer=''):
#         if cart is None:
#             cart = []
#         self.cart = cart
#         self.customer = customer
#
#     def __add__(self, other):
#         return Order(self.cart.append(other), self.customer)
#
#     def __radd__(self, other):
#         return Order(self.cart + other, self.customer)
#
#     def __sub__(self, other):
#         return Order(self.cart.remove(other), self.customer)
#
#     def __rsub__(self, other):
#         return Order(self.cart.remove(other), self.customer)
#
#
# order = Order(['banana', 'apple'], 'Гена Букин')
# print(order.__dict__)
# order_2 = order + 'orange'
# print(order.cart)
# assert order.cart == ['banana', 'apple']
# assert order.customer == 'Гена Букин'
# assert order_2.cart == ['banana', 'apple', 'orange']
#
# order = 'mango' + order
# assert order.cart == ['mango', 'banana', 'apple']
# order = 'ice cream' + order
# assert order.cart == ['ice cream', 'mango', 'banana', 'apple']
#
# order = order - 'banana'
# assert order.cart == ['ice cream', 'mango', 'apple']
#
# order3 = order - 'banana'
# assert order3.cart == ['ice cream', 'mango', 'apple']
#
# order = order - 'mango'
# assert order.cart == ['ice cream', 'apple']
# order = 'lime' - order
# assert order.cart == ['ice cream', 'apple']
# print('Good')
# from tkinter import *
# import random
#
# okno = Tk()
# okno.geometry('500x300')
# okno.title('Магический шар')
#
# cnucok = ['шанс есть', 'да', 'нет', 'не самое лушшее время', 'лучше подождать',
# 'если решено, лучше не медлить', 'да, да и ещё раз да', 'ни в коем случае', 'попробуй!)',
# 'риск дело благородное',
# 'перефразируй вопрос', 'ты и так знаешь как нужно поступить', 'лучше не стоит', 'ни в коем случае',
# 'действуй, не тупи', 'это ничего не изменит', 'это нужно спланировать', 'советую не торопиться', 'посоветуйся
# с близкими', 'проконсультируйся со специалистом',
# 'бездействие, тоже действие', 'что бы ты сам посоветовал в этом случае', 'уже не важно', 'чем быстрее тем лучше',
# 'сначала разберись с другими проблемами', 'спроси об этом чуть позже', 'это мне не известно',
# 'хорошие перспективы', 'весьма сомнительно', 'это не то о чём надо переживать',
# 'чем скорее это случится, тем лучше']
#
# klik = 0
# def kubik6():
# 	global klik
# 	klik = random.sample(cnucok, 1)
# 	kno['text'] = klik
# 	text6 = Label(okno, text = 'Кубик D6:' + str(klik), bg = 'darkgray')
# 	aaa = Label(okno, text = klik, bg = 'darkgray').grid(row=0, column=0)
#
# kno = Button(okno)
# kno.configure(bg = 'gray', fg = 'yellow', text = klik, command = kubik6)
# kno.grid(row=1, column=1)
#
#
#
# #Возьми кредит! Черный лебедь в поле зрения Возможность сесть на мель Потеря денег
# #Проверь
#
# okno.mainloop()
# from tkinter import *
# from tkinter import ttk
# import tkinter.messagebox
#
# okno = Tk()
#
# # okno.resizable(False, False)
# okno.geometry('500x300')
# okno.title('Виджеты')
# okno.configure(bg='darkgray')
# okno.wm_attributes('-alpha', 1)
#
# # Меню
# mmm = Menu()
# okno.config(menu=mmm)
# mmm1 = Menu()
#
# mmm1.add_command(label='Меню 123')
# mmm1.add_command(label='Меню 456')
# mmm1.add_command(label='Меню 789')
# # mmm.add_command(label='Меню 1', menu = mmm1)
# mmm.add_command(label='Меню 2')
# mmm.add_command(label='Меню 3')
# mmm.add_command(label='Меню 4')
# mmm.add_command(label='Меню 5')
#
#
# # одноразовая кнопка
# def nad():
#     kno3['text'] = 'Нажал)'
#
#
# # ввод и сохранение логина и пароля
# def dannie():
#     print(login.get())
#     print(type(password.get()))
#     print(type(login.get()))
#     print(password.get())
#     login.delete(0, 9)
#     password.delete(0, 9)
#
#
# # отметить все галочки
# def vse_gal():
#     for i in [gal]:
#         i.select()
#
#
# # отменить все галочки
# def nevse_gal():
#     for i in [gal]:
#         i.deselect()
#
#
# # выбери другой город
# def gorod1():
#     gorod.set('Другой Город')
#
#
# # Всплывающие окна
# def vspliv():
#     tkinter.messagebox.showwarning('Заголовок 1', 'Текст 1')
#     tkinter.messagebox.showerror('Заголовок 2', 'Текст 2')
#     tkinter.messagebox.askquestion('Заголовок 3', 'Текст 3')
#     tkinter.messagebox.showinfo('Заголовок 4', 'Текст 4')
#     tkinter.messagebox.askokcancel('Заголовок 5', 'Текст 5')
#     tkinter.messagebox.askretrycancel('Заголовок 6', 'Текст 6')
#     tkinter.messagebox.askyesnocancel('Заголовок 7', 'Текст 7')
#
#
# # t1 = Label(okno, text = 'Тут есть разные Виджеты', bg = 'darkblue', fg = 'white', font = ('Arial', 20, 'bold'))
# # t1.config(font = ('Verdana', 25))
# # t1.place(x = 50, y = 50)
# # t1.grid(row=0, column=0, columnspan=3)
#
# kladka = ttk.Notebook()
# kladka.grid(row=0, column=0)
# frame1 = ttk.Frame(kladka)
# frame2 = ttk.Frame(kladka)
# frame1.grid(row=1, column=0)
# frame2.grid(row=2, column=0)
#
# # logo2 = PhotoImage(file="./картинки/klad2.png")
# kladka.add(frame1, text=' вкладка 1')
# kladka.add(frame2, text='вкладка 2')
#
# kno3 = Button(okno, text='Жми!', command=nad, )
# kno3.grid(row=1, column=1)
#
# box = Button(okno, text='Всплыв', command=vspliv)
# box.grid(row=2, column=1)
#
# login1 = Label(okno, text='Логин:', bg='darkgray')
# login1.grid(row=3, column=0)
# password1 = Label(okno, text='Пароль:', bg='darkgray')
# password1.grid(row=4, column=0)
#
# login = Entry(okno)
# login.grid(row=3, column=1)
# password = Entry(okno, show='*')
# password.grid(row=4, column=1)
#
# sabmit = Button(okno, text='Войти', command=dannie)
# sabmit.grid(row=5, column=1)
#
# data = ttk.Spinbox(from_=1.0, to=31.0)
# data.grid(row=5, column=0)
#
# rpomkoctb1 = IntVar(value=50)
# Label(textvariable=rpomkoctb1).grid(row=6, column=0)
# rpomkoctb = ttk.Scale(orient=HORIZONTAL, length=200, from_=1.0, to=100.0, variable=rpomkoctb1)
# rpomkoctb.grid(row=7, column=0)
#
# # Шкала прогресса
# aaa = ttk.Progressbar(okno, orient='horizontal', length=150, value=20, mode="indeterminate")
# aaa.grid(row=8, column=0)
# # def start():
# #	aaa.start(1000)
# ctapt = Button(okno, text='CTAPT', command=aaa.start).grid(row=9, column=0)
# ctop = Button(okno, text='CT0n', command=aaa.stop).grid(row=10, column=0)
#
# for i in range(1, 6):
#     gal = Checkbutton(okno, text='Галочка № ' + str(i))
#     gal.grid(row=i, column=3)
# gal1 = Checkbutton(okno, text='В.Дави', indicatoron=False, bd=5)
# gal1.grid(row=0, column=3)
# Button(okno, text='Поставить все', command=vse_gal).grid(row=6, column=3)
# Button(okno, text='Убрать все', command=nevse_gal).grid(row=7, column=3)
#
# Label(okno, text='Выбор варианта').grid(row=1, column=2)
# varik = IntVar()
# sas = IntVar()
# Radiobutton(okno, text='Первый', variable=varik, value=1).grid(row=2, column=2)
# Radiobutton(okno, text='Второй', variable=sas, value=2).grid(row=3, column=2)
# Radiobutton(okno, text='Третий', variable=varik, value=3).grid(row=4, column=2)
#
# # Label(okno, text = 'Выбери Город', bg = 'darkgray').grid(row=1, column=0)
# Button(okno, text='Нет моего города', command=gorod1).grid(row=1, column=0)
# goroda = (
# 'Москва', 'Санкт-Петербург', 'Великий Новгород', 'Нижний Новгород', 'Краснодар', 'Липецк', 'Воронеж', 'Вологда')
# gorod = ttk.Combobox(okno, values=goroda)
# gorod.current(1)
# gorod.grid(row=2, column=0)
#
# okno.mainloop()
# from tkinter import *
#
# okno = Tk()
#
# # ³²√
# okno.resizable(False, False)
# okno.geometry('500x300')
# okno.title('окно с кнопкой')
# okno.configure(bg='darkblue')
# okno.wm_attributes('-alpha', 0.9)
# # okno.iconbitmap('C:/Users/ва/Desktop/прога/иконка.ico')
# # okno.iconbitmap('C:/Users/Sveta/Desktop/Максим/комп/прога/иконка.ico')
# # okno.iconbitmap(r'C:\Users\Sveta\Desktop\Максим\комп\прога\иконка.ico')
#
# klik = 0
#
#
# def kno_cmd():
#     global klik
#     klik += 1
#     kno['text'] = klik
#     kno2['text'] = 'Квадрат\nчисла\n' + str(klik ** 2)
#     knoky6['text'] = klik ** 3
#
#
# def nad():
#     print('111')
#     kno3['text'] = '777'
#
#
# kno3 = Button(okno, text='333', command=nad, )
# kno3.pack()
#
# t1 = Label(okno, text='Квадрат ', bg='blue', fg='white')
# t1.config(font=('Verdana', 25))
# t1.place(x=50, y=50)
# t1.pack()
#
# t3 = Label(okno, text='222 ', bg='blue', fg='white')
# t3.config(font=('Verdana', 25))
# t3.pack()
#
# kno = Button(okno)
# kno.configure(bg='gray', fg='yellow', text=klik, command=kno_cmd)
# kno.place(x=30, y=180, width=150, height=100)
# t2 = Label(kno, text='КНОПКА', bg='gray', fg='red')
# t2.config(font=('Verdana', 20))
# t2.pack()
#
# kno2 = Button(okno)
# kno2.configure(bg='black', fg='white', text='привет', command=kno_cmd)
# kno2.place(x=60, y=20, width=50, height=150)
#
# knoky6 = Button(okno)
# knoky6.place(x=260, y=200, width=100, height=50)
# knoky6.configure(bg='red', fg='black', command=kno_cmd)
#
# okno.mainloop()
# from tkinter import *
# from tkinter import ttk
# import tkinter.messagebox
# import random
#
# okno = Tk()
#
# # okno.resizable(False, False)
# okno.geometry('500x300')
# okno.title('Камень Ножницы Бумага')
# okno.configure(bg='darkgray')
# okno.wm_attributes('-alpha', 1)
#
# knb = ['Камень', 'Ножницы', 'Бумага']
# aaa = random.sample(knb, 1)
#
#
# def tvoik():
#     tekct.delete(0, END)
#     tekct.insert(0, knb[0])
#     Label(okno, text='Камень', bg='darkgray').place(x=230, y=50)
#     print(knb[0], knb[1], knb[2], str(*aaa), *aaa)
#     #	print(knb[0], tekct.get(), aaa, type(tekct.get()), type(aaa), str(aaa),
#     #		type(str(aaa)), list(tekct.get()), type(list(tekct.get())))
#     if knb[0] == str(*aaa):
#         Label(okno, text='Ничья', bg='darkgray').place(x=130, y=150)
#     elif knb[1] == str(*aaa):
#         Label(okno, text='Ты Выйграл', bg='darkgray').place(x=130, y=150)
#     elif knb[2] == str(*aaa):
#         Label(okno, text='Ты Проиграл', bg='darkgray').place(x=130, y=150)
#         print('заебись 1')
#
#
# def tvoin():
#     tekct.delete(0, END)
#     tekct.insert(0, knb[1])
#     Label(okno, text='Ножницы', bg='darkgray').place(x=230, y=50)
#     if knb[1] == str(*aaa):
#         Label(okno, text='Ничья', bg='darkgray').place(x=130, y=150)
#     elif knb[2] == str(*aaa):
#         Label(okno, text='Ты Выйграл', bg='darkgray').place(x=130, y=150)
#     elif knb[0] == str(*aaa):
#         Label(okno, text='Ты Проиграл', bg='darkgray').place(x=130, y=150)
#         print('заебись 2')
#
#
# def tvoib():
#     tekct.delete(0, END)
#     tekct.insert(0, knb[2])
#     Label(okno, text='Бумага', bg='darkgray').place(x=230, y=50)
#     if knb[2] == str(*aaa):
#         Label(okno, text='Ничья', bg='darkgray').place(x=130, y=150)
#     elif knb[0] == str(*aaa):
#         Label(okno, text='Ты Выйграл', bg='darkgray').place(x=130, y=150)
#     elif knb[1] == str(*aaa):
#         Label(okno, text='Ты Проиграл', bg='darkgray').place(x=130, y=150)
#         print('заебись 3')
#
#
# #	Label(okno, text = k['text'], bg = 'darkgray').place(x = 200, y = 50)
# def netvoi():
#     #	qqq = random.sample(knb, 1)
#     Label(okno, text=aaa, bg='darkgray').place(x=230, y=100)
#     print(aaa, type(aaa))
#     vvod["text"] = tekct.get()
#
#
# #	vvod["text"] = k.get()
# # if qqq == k['text']:
# # 	print('eeee')  type(k['text'])
#
# def kkk():
#     pass
#
#
# # if aaa == 'Камень':
#
# Label(okno, text='Выбери - ', bg='darkgray').place(x=100, y=10)
#
# vvod = Label()
# vvod.place(x=10, y=10)
#
# tekct = Entry(okno, width=33)
# tekct.place(x=200, y=10)
#
# Label(okno, text='Ты выбрал:', bg='darkgray').place(x=100, y=50)
# Label(okno, text='Компьютер выбрал:', bg='darkgray').place(x=100, y=100)
#
# k = Button(okno, command=tvoik, text='Камень', bg='darkgray').place(x=300, y=200, width=50, height=30)
# n = Button(okno, command=tvoin, text='Ножницы', bg='darkgray').place(x=400, y=150, width=50, height=30)
# b = Button(okno, command=tvoib, text='Бумага', bg='darkgray').place(x=400, y=250, width=50, height=30)
#
# tt = Button(okno, command=netvoi, text='komn', bg='darkgray').place(x=230, y=250, width=50, height=30)
#
# okno.mainloop()
# from tkinter import *
# import time
# import random
#
# a = ['red', 'green', 'blue', 'black', 'Orange', 'Violet', 'Pink', 'White']
#
#
# def close():
#     global run
#     run = False
#
#
# klik = 0
#
#
# def nad():
#     global klik
#     run = True
#     r = random.randint(10, 25)
#     ckopoctb_x = random.randint(-10, 10)
#     ckopoctb_y = random.randint(-10, 10)
#     print(ckopoctb_x, ckopoctb_y, klik)
#     kno3['text'] = 'БАХ'
#     lllap = x3.create_oval(x - r, y - r, x + r, y + r, width=3, fill=random.choice(a), outline=random.choice(a))
#     for i in range(100):
#         klik += 1
#         x3.move(lllap, ckopoctb_x, ckopoctb_y)
#         coords = x3.coords(lllap)
#         okno.update()
#         time.sleep(0.01)
#         klik -= 1
#         c4et4ik = Label(okno, text=klik, bg='blue', fg='white').place(x=60, y=80, width=50, height=50)
#
#
# aaa = random.randint(1, 100)
# x = 500
# y = 500
#
# okno = Tk()
# okno.config(width=1000, height=1000)
# okno.protocol('WM_DELETE_WINDOW', close)
#
# x3 = Canvas(okno, bg='darkgray')
# x3.place(width=1000, height=1000)
#
# # lllap = x3.create_oval(x-r, y-r, x+r, y+r, width = 3, fill = 'red', outline = 'black')
#
# kno3 = Button(okno, text='ШАРЫ', command=nad)
# kno3.place(x=475, y=475, width=50, height=50)
#
# run = True
# while run:
#     # x3.move(lllap, ckopoctb, 0)
#     # coords = x3.coords(lllap)
#
#     okno.update()
#     time.sleep(0.01)
#
# okno.destroy()
# from tkinter import *
# import random
#
# okno = Tk()
# okno.geometry('500x300')
# okno.title('Генератор Безопасных паролей')
#
# # A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
# # a b c d e f g h i j k l m n o p q r s t u v w x y z
# # а, б, в, г, д, е, ё, ж, з, и, й, к, л, м, н, о, п, р, с, т, у, ф, х, ц, ч, ш, щ, ъ, ы, ь, э, ю, я.
# # АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ;
# # А Б В Г Д Е Ё Ж З И Й К Л М Н О П Р С Т У Ф Х Ц Ч Ш Щ Ъ Ы Ь Э Ю Я;
# # А, Б, В, Г, Д, Е, Ё, Ж, З, И, Й, К, Л, М, Н, О, П, Р, С, Т, У, Ф, Х, Ц, Ч, Ш, Щ, Ъ, Ы, Ь, Э, Ю, Я;
# # ЯЮЭЬЫЪЩШЧЦХФУТСРПОНМЛКЙИЗЖЁЕДГВБА.
# # абвгдеёжзийклмнопрстуфхцчшщъыьэюя;
# # а б в г д е ё ж з и й к л м н о п р с т у ф х ц ч ш щ ъ ы ь э ю я;
# #  ! " # $ % & ' ( ) * + , - . / : ; < = > ? @ [ \ ] ^ _` { | } ~
#
# dbukva = 'abcdefghijklmnopqrstuvwxyz'
# d10 = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
# dznak = '!"#$%&()*+,-./:;<=>?@[]^_`{|}~'
# dbig = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# vse = [dbukva, d10, dznak, dbig]
#
#
# def dannie():
#     print(login.get())
#     print(type(password.get()))
#     print(type(login.get()))
#     print(password.get())
#     login.delete(0, 9)
#     password.delete(0, 9)
#
#
# def zvezda():
#     pass
#
#
# # def add(cifra):
# # 	value = vvod.get()
# # 	if value[0]=='0' and len(value)==1:
# # 		value = value[1:]
#
# def bukva():
#     a = random.choice(dbukva)
#     vvod.insert(-1, a)
#
#
# def cifra():
#     a = random.randrange(1, 11)
#     vvod.insert(-1, a)
#
#
# def znak():
#     a = random.choice(dznak)
#     vvod.insert(-1, a)
#
#
# def big():
#     a = random.choice(dbig)
#     vvod.insert(-1, a)
#
#
# def general():
#     nap = ''
#     vvod.delete(0, END)
#     for i in range(8):
#         nap += random.choice(random.choice(vse))
#     vvod1['text'] = nap
#     vvod.insert(0, nap)
#     print(nap)
#
#
# def npovepka():
#     a = []
#     q = ['Буквы', 'Цыфры', 'Знака', 'Заглавной буквы']
#     for j in range(4):
#         for i in range(len(vse[j])):
#             if vse[j][i] in vvod.get():
#                 a.append(j)
#                 print(vvod.get(), j, a)
#                 break
#     if len(a) == 4 and len(vvod.get()) > 7:
#         vvod2['text'] = 'Пароль Надёжный'
#         vvod3['text'] = ''
#         #	vvod3.delete(0, END)
#         print('gagaga')
#     else:
#         vvod2['text'] = 'Пароль Ненадёжный:'
#
#     for i in range(4):
#         if i not in a:
#             vvod3['text'] = 'Нехватает ' + q[i]
#
#
# # 		# and vvod.get() in d10 and vvod.get() in d10 and vvod.get() in d10 and :
# # 			print(vvod.get(), type(vvod.get()))
#
# # + str(cifra)
# # vvod.delete(0,tk.END)
# # vvod.insert(0, value+cifra)
#
#
# # def kno(cifra):
# #  	return Button(text=cifra, bd=5, font=20, command=lambda : add(cifra))
#
# login1 = Label(okno, text='Логин:', bg='darkgray')
# login1.grid(row=0, column=0)
# password1 = Label(okno, text='Пароль:', bg='darkgray')
# password1.grid(row=1, column=0)
#
# login = Entry(okno)
# login.grid(row=0, column=1)
# password = Entry(okno, show='*')
# password.grid(row=1, column=1)
#
# sabmit = Button(okno, text='Войти', command=dannie)
# sabmit.grid(row=2, column=0)
#
# # kno('Буква').grid(row=0, column=2)
# # kno('Цифра').grid(row=1, column=2)
# # kno('Знак').grid(row=2, column=2)
# # kno('Заглавная').grid(row=3, column=2)
#
# kno = Button(okno, text='Буква', command=bukva)
# kno.grid(row=0, column=2)
# kno2 = Button(okno, text='Цифра', command=cifra)
# kno2.grid(row=1, column=2)
# kno3 = Button(okno, text='Знак', command=znak)
# kno3.grid(row=2, column=2)
# kno4 = Button(okno, text='Заглавная', command=big)
# kno4.grid(row=3, column=2)
#
# vvod = Entry(okno)
# vvod.grid(row=4, column=0, columnspan=4)
#
# knov = Button(okno, text='Проверка пароля', command=npovepka)
# knov.grid(row=5, column=1)
# knor = Button(okno, text='Генерация пароля', command=general)
# knor.grid(row=5, column=2)
#
# vvod1 = Label()
# vvod1.grid(row=5, column=3)
# vvod2 = Label()
# vvod2.grid(row=6, column=1)
# vvod3 = Label()
# vvod3.grid(row=6, column=2)
#
# okno.mainloop()
# from faker import Faker
# from tkinter import *
# import random
# import openpyxl
#
# klik = 0
#
#
# def fake():
#     vvod.delete(0, END)
#     vvod1.delete(0, END)
#     vvod2.delete(0, END)
#     vvod3.delete(0, END)
#     vvod4.delete(0, END)
#     vvod5.delete(0, END)
#     vvod6.delete(0, END)
#     vvod7.delete(0, END)
#     vvod8.delete(0, END)
#     vvod9.delete(0, END)
#     vvod10.delete(0, END)
#
#     vvod.insert(0, pyc.name())
#     vvod1.insert(0, pyc.address())
#     vvod2.insert(0,
#     str(random.randint(1, 28)) + '.' + str(random.randint(1, 12)) + '.' + str(random.randint(1966, 2004)))
#     vvod3.insert(0, pyc.company())
#     vvod4.insert(0, pyc.job())
#     vvod5.insert(0, pyc.phone_number())
#     vvod6.insert(0, pyc.ascii_free_email())
#     vvod7.insert(0,
#     pyc.credit_card_number() + '   ' + pyc.credit_card_expire() + '   ' + pyc.credit_card_security_code())
#     vvod8.insert(0, str(random.randint(1000, 10000)) + '   ' + str(random.randint(100000, 1000000)))
#     vvod9.insert(0, pyc.uri())
#     vvod10.insert(0, pyc.hostname())
#     print(klik)
#
#
# # def fake():
# # 	f1 = Label(okno, justify = LEFT, text = pyc.name(), bg = 'darkgray')
# # 	f1.grid(row=0, column=1, sticky = W)
# # 	Label(okno, justify = LEFT, text = pyc.address(), bg = 'darkgray').grid(row=1, column=1, sticky = W)
# # 	Label(okno, justify = LEFT, text = str(random.randint(1, 28)) + '.' + str(random.randint(1, 12))
# + '.' + str(random.randint(1966, 2004)), bg = 'darkgray').grid(row=2, column=1, sticky = W)
# # 	Label(okno, justify = LEFT, text = pyc.company(), bg = 'darkgray').grid(row=3, column=1, sticky = W)
# # 	Label(okno, justify = LEFT, text = pyc.job(), bg = 'darkgray').grid(row=4, column=1, sticky = W)
# # 	Label(okno, justify = LEFT, text = pyc.phone_number(), bg = 'darkgray').grid(row=5, column=1, sticky = W)
# # 	Label(okno, justify = LEFT, text = pyc.ascii_free_email() , bg = 'darkgray').grid(row=6, column=1, sticky = W)
# # 	Label(okno, justify = LEFT, text = pyc.credit_card_number() + '   ' + pyc.credit_card_expire() + '
# ' + pyc.credit_card_security_code(), bg = 'darkgray').grid(row=7, column=1, sticky = W)
# # 	Label(okno, justify = LEFT, text = str(random.randint(1000, 10000)) + '   '
# + str(random.randint(100000, 1000000)), bg = 'darkgray').grid(row=8, column=1, sticky = W)
# # 	Label(okno, justify = LEFT, text = pyc.uri(), bg = 'darkgray').grid(row=9, column=1, sticky = W)
# # 	Label(okno, justify = LEFT, text = pyc.hostname(), bg = 'darkgray').grid(row=10, column=1, sticky = W)
# # 	#return f1
# # 	print(klik)
#
#
# ttt = openpyxl.Workbook()
#
#
# def cozdatb():
#     # ttt = openpyxl.Workbook()
#     sheet = ttt.active
#     sheet['A1'] = 'Ф И О:'
#     sheet['B1'] = 'Номер телефона:'
#     sheet['C1'] = 'Адрес:'
#     sheet['D1'] = 'E-MAIL:'
#     ttt.save('aaaa.xlsx')
#     ttt.close()
#
#
# def dob():
#     global klik
#     klik += 1
#     # ttt = openpyxl.Workbook()
#     sheet = ttt.active
#     sheet.cell(row=2 + klik, column=1).value = vvod.get()
#     sheet.cell(row=2 + klik, column=2).value = vvod5.get()
#     sheet.cell(row=2 + klik, column=3).value = vvod1.get()
#     sheet.cell(row=2 + klik, column=4).value = vvod6.get()
#     ttt.save('aaaa.xlsx')
#     print(klik)
#
#
# okno = Tk()
#
# # okno.resizable(False, False)
# okno.geometry('500x300')
# okno.title('Личность')
# okno.configure(bg='darkgray')
# okno.wm_attributes('-alpha', 1)
#
# pyc = Faker("ru_RU")
# a = Faker()
# q = '::'
#
# vvod = Entry(okno, width=30)
# vvod.grid(row=0, column=1)
# vvod1 = Entry(okno, width=30)
# vvod1.grid(row=1, column=1)
# vvod2 = Entry(okno, width=30)
# vvod2.grid(row=2, column=1)
# vvod3 = Entry(okno, width=30)
# vvod3.grid(row=3, column=1)
# vvod4 = Entry(okno, width=30)
# vvod4.grid(row=4, column=1)
# vvod5 = Entry(okno, width=30)
# vvod5.grid(row=5, column=1)
# vvod6 = Entry(okno, width=30)
# vvod6.grid(row=6, column=1)
# vvod7 = Entry(okno, width=30)
# vvod7.grid(row=7, column=1)
# vvod8 = Entry(okno, width=30)
# vvod8.grid(row=8, column=1)
# vvod9 = Entry(okno, width=30)
# vvod9.grid(row=9, column=1)
# vvod10 = Entry(okno, width=30)
# vvod10.grid(row=10, column=1)
#
# pyc.credit_card_number(),
#
# Label(okno, justify=LEFT, text='Ф И О:', bg='darkgray').grid(row=0, column=0, sticky=W)
# Label(okno, justify=LEFT, text='Адрес:', bg='darkgray').grid(row=1, column=0, sticky=W)
# Label(okno, justify=LEFT, text='Дата Рождения:', bg='darkgray').grid(row=2, column=0, sticky=W)
# Label(okno, justify=LEFT, text='Место Работы:', bg='darkgray').grid(row=3, column=0, sticky=W)
# Label(okno, justify=LEFT, text='Должность:', bg='darkgray').grid(row=4, column=0, sticky=W)
# Label(okno, justify=LEFT, text='Номер телефона:', bg='darkgray').grid(row=5, column=0, sticky=W)
# Label(okno, justify=LEFT, text='E-MAIL:', bg='darkgray').grid(row=6, column=0, sticky=W)
# Label(okno, justify=LEFT, text='№ Карты, Срок действия, CVV/CVC код:', bg='darkgray').grid(row=7, column=0, sticky=W)
# Label(okno, justify=LEFT, text='Серия и номер паспорта:', bg='darkgray').grid(row=8, column=0, sticky=W)
# Label(okno, justify=LEFT, text='Дополнитеньная найденная информация:', bg='darkgray').grid(row=9, column=0, sticky=W)
# Label(okno, justify=LEFT, text='Последний посещённый сайт:', bg='darkgray').grid(row=10, column=0, sticky=W)
#
# kno = Button(okno, text='Найти', command=fake)
# kno.grid(row=12, column=0)
#
# kno1 = Button(okno, text='Создать', command=cozdatb)
# kno1.grid(row=13, column=0)
#
# kno2 = Button(okno, text='Добавить', command=dob)
# kno2.grid(row=12, column=1)
#
# kno11 = Button(okno, text='11111111', command=dob)
# kno11.grid(row=12, column=2)
# kno12 = Button(okno, text='22222222', command=dob)
# kno12.grid(row=12, column=3)
#
# okno.mainloop()
# from tkinter import *
# import turtle
# from turtle import *
# import tkinter.messagebox
#
# color = ['red', 'black', 'green', 'blue', 'yellow', 'purple', 'white', 'brown', 'cyan', 'gray', 'pink', 'indigo']
# forma = ['arrow', 'turtle', 'circle', 'square', 'triangle', 'classic']
#
#
# # tur.shape()
#
# # def puc():
# # 	turtle.ondrag(okno, btn=1, add=False)
#
# def ocb(x, y, m):
#     docka.create_line(x / 2 - 100, 0 - 100, x / 2 - 100, y)
#     docka.create_line(0 - 100, y / 2 - 100, x, y / 2 - 100)
#     for i in range(-100, max(x, y), m):
#         docka.create_line(i, y / 2 - 100 - 10, i, y / 2 - 100 + 10)
#         docka.create_line(x / 2 - 10 - 100, i, x / 2 + 10 - 100, i)
#
#
# # ЦВЕТА
#
# def cmena(color):
#     pass
#
#
# # def col0(i):
# # 	tur.color(color[i])
# # 	print(i)
# def zalivka():
#     fillcolor(color[0])
#
#
# def col0():
#     tur.color(color[0])
#
#
# def col1():
#     tur.color(color[1])
#
#
# def col2():
#     tur.color(color[2])
#
#
# def col3():
#     tur.color(color[3])
#
#
# def col4():
#     tur.color(color[4])
#
#
# def col5():
#     tur.color(color[5])
#
#
# def col6():
#     tur.color(color[6])
#
#
# def col7():
#     tur.color(color[7])
#
#
# def col8():
#     tur.color(color[8])
#
#
# def col9():
#     tur.color(color[9])
#
#
# def co20():
#     tur.color(color[10])
#
#
# def co21():
#     tur.color(color[11])
#
#
# # ДВИЖЕНИЕ
#
# def lin():
#     tur.forward(50)
#
#
# def npavo():
#     tur.right(90)
#
#
# def levo():
#     tur.left(90)
#
#
# def dvij(event):
#     if event.keysym == 'Up':
#         tur.forward(int(data.get()))
#     elif event.keysym == 'Right':
#         tur.right(90)
#     elif event.keysym == 'Left':
#         tur.left(90)
#     elif event.keysym == 'Down':
#         tur.backward(30)
#         print(data.get(), type(data.get(), ))
#
#
# # ФУНКЦИИ
#
# def delete():
#     tur.undo()
#
#
# def clear():
#     vvv = tkinter.messagebox.askokcancel('Внимание', 'Удалить этот прекрасный рисунок?')
#     if vvv:
#         tur.clear()
#
#
# def dom():
#     tur.home()
#
#
# def nep0():
#     tur.up()
#
#
# def nep1():
#     tur.down()
#
#
# # ПАРАМЕТРЫ
#
# def ckopoctb():
#     pass
#
#
# def pazmep1():
#     tur.pensize(1)
#
#
# def pazmep3():
#     tur.pensize(3)
#
#
# def pazmep5():
#     tur.pensize(5)
#
#
# def pazmep7():
#     tur.pensize(7)
#
#
# def pazmep10():
#     tur.pensize(10)
#
#
# # ФИГУРЫ
# def kpyr():
#     tur.circle(50)
#
#
# def kva():
#     for i in range(4):
#         tur.forward(100)
#         tur.right(90)
#
#
# # ИЗМЕРЕНИЯ
#
# def kopd():
#     print(tur.pos())
#

#

#
# docka = Canvas(okno, bg='darkgray')
# docka.place(width=700, height=700)
#
# # okno = turtle.Screen()
# tur = RawTurtle(docka, )
# tur.penup()
# tur.setx(150)
# tur.sety(-150)
# tur.pendown()

# # kn = Button(okno, command = puc, text = 'puc')
# # kn.place(x = 725, y = 50, width = 50, height = 30)
#
# knoqq = Button(okno, command=ocb(500, 500, 20), text='ocb')
# knoqq.place(x=725, y=100, width=50, height=30)
# knoqm = Button(okno, command=dom, text='Дом')
# knoqm.place(x=725, y=70, width=50, height=30)
# # ocb(500, 500, 20)
#
# kno = Button(okno, command=lin, text='--->')
# kno.place(x=725, y=260, width=50, height=30)
# kno5 = Button(okno, command=lin, text='<---')
# kno5.place(x=725, y=200, width=50, height=30)
# kno2 = Button(okno, command=levo, text='влево')
# kno2.place(x=700, y=230, width=50, height=30)
# kno3 = Button(okno, command=npavo, text='вправо')
# kno3.place(x=750, y=230, width=50, height=30)
#
# okno.bind("<Key>", dvij)
#
# kno4 = Button(okno, command=delete, text='Назад')
# kno4.place(x=750, y=150, width=50, height=30)
# kno6 = Button(okno, command=clear, text='Удалить')
# kno6.place(x=700, y=150, width=50, height=30)
#
# # Checkbutton(okno, command = zalivka, text = '#', bg = 'red').place(x = 750, y = 300, width = 30, height = 30)
# # for i in range(4):
# # 	Button(okno, command = lambda : col0(i), text = i, bg = 'red').place(x = 700, y = 300 + i*30,
# width = 30, height = 30)
# Button(okno, command=col0, text='крас', bg='red').place(x=700, y=300 + 0 * 30, width=30, height=30)
# Button(okno, command=col1, text='чёр', bg='black', fg='white').place(x=700, y=300 + 1 * 30, width=30, height=30)
# Button(okno, command=col2, text='зел', bg='green').place(x=700, y=300 + 2 * 30, width=30, height=30)
# Button(okno, command=col3, text='син', bg='blue', fg='white').place(x=700, y=300 + 3 * 30, width=30, height=30)
# Button(okno, command=col4, text='Ж', bg='yellow').place(x=730, y=300 + 0 * 30, width=30, height=30)
# Button(okno, command=col5, text='Фи', bg='purple', fg='white').place(x=730, y=300 + 1 * 30, width=30, height=30)
# Button(okno, command=col6, text='бел', bg='white').place(x=730, y=300 + 2 * 30, width=30, height=30)
# Button(okno, command=col7, text='кор', bg='brown', fg='white').place(x=730, y=300 + 3 * 30, width=30, height=30)
# Button(okno, command=col8, bg='cyan').place(x=760, y=300 + 0 * 30, width=30, height=30)
# Button(okno, command=col9, bg='gray', fg='white').place(x=760, y=300 + 1 * 30, width=30, height=30)
# Button(okno, command=co20, bg='pink').place(x=760, y=300 + 2 * 30, width=30, height=30)
# Button(okno, command=co21, bg='indigo', fg='white').place(x=760, y=300 + 3 * 30, width=30, height=30)
#
# Button(okno, command=col0, text='<', bg='darkgray').place(x=720, y=450, width=30, height=30)
# Button(okno, command=ckopoctb, text=tur.speed(), bg='darkgray').place(x=750, y=450, width=30, height=30)
#
# Button(okno, command=pazmep1, text='1', bg='darkgray').place(x=700, y=480, width=20, height=20)
# Button(okno, command=pazmep3, text='3', bg='darkgray').place(x=720, y=480, width=20, height=20)
# Button(okno, command=pazmep5, text='5', bg='darkgray').place(x=740, y=480, width=20, height=20)
# Button(okno, command=pazmep7, text='7', bg='darkgray').place(x=760, y=480, width=20, height=20)
# Button(okno, command=pazmep10, text='10', bg='darkgray').place(x=780, y=480, width=20, height=20)
#
# data = Spinbox(from_=1.0, to=31.0)
# data.place(x=700, y=500)
#
# knepo = Button(okno, command=nep0, text='без')
# knepo.place(x=700, y=530, width=50, height=30)
# knep1 = Button(okno, command=nep1, text='след')
# knep1.place(x=750, y=530, width=50, height=30)
#
# Button(okno, command=kpyr, text='O').place(x=550, y=730, width=50, height=30)
# Button(okno, command=kva, text='[]').place(x=500, y=730, width=50, height=30)
#
# Button(okno, command=kopd, text='Где').place(x=400, y=730, width=50, height=30)
#
# okno.exitonclick()
# from tkinter import *
# import main
#
# okno = Tk()
#
#
# # okno.resizable(False, False)
# okno.geometry('500x300')
# okno.title('Личность')
# okno.configure(bg='darkgray')
# okno.wm_attributes('-alpha', 1)
#
# Button(okno, command=______, text='Где').place(x=200, y=230, width=50, height=30)
#
#
# vvod = Entry(okno)
# vvod.place(x=300, y=230)
# Напишите определение класса Order
# Напишите определение класса Order
# class Order:
#     def __init__(self, cart=None, customer=''):
#         self.cart = cart
#         self.customer = customer
#
#     def __add__(self, other):
#         return Order(self.cart + other.split(), self.customer)
#
#     def __radd__(self, other):
#         return Order([other] + self.cart, self.customer)
#
#     def __sub__(self, other):
#         if other in self.cart:
#             self.cart.remove(other)
#             return Order(self.cart, self.customer)
#         return Order(self.cart, self.customer)
#
#     def __rsub__(self, other):
#         return Order(self.cart, self.customer)
#
#
# # Ниже код для проверки методов класса Order
#
# order = Order(['banana', 'apple'], 'Гена Букин')
#
# order_2 = order + 'orange'
# assert order.cart == ['banana', 'apple']
# assert order.customer == 'Гена Букин'
# assert order_2.cart == ['banana', 'apple', 'orange']
#
# order = 'mango' + order
# print(order.cart)
# assert order.cart == ['mango', 'banana', 'apple']
# order = 'ice cream' + order
# print(order.cart)
# assert order.cart == ['ice cream', 'mango', 'banana', 'apple']
#
# order = order - 'banana'
# assert order.cart == ['ice cream', 'mango', 'apple']
#
# order3 = order - 'banana'
# assert order3.cart == ['ice cream', 'mango', 'apple']
#
# order = order - 'mango'
# assert order.cart == ['ice cream', 'apple']
# order = 'lime' - order
# assert order.cart == ['ice cream', 'apple']
# print('Good')
# class Test:
#     def __init__(self, name):
#         self.name = name
#
#     @staticmethod
#     def get_test():
#         return 2 * 2
# print(Test.get_test())
# print(23232.__name__)
# Напишите определение класса Hero
# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def __add__(self, other):
#         if isinstance(other, Rectangle):
#             return Rectangle(self.width + other.width + self.height + other.height)
#
#     def __str__(self):
#         return f'Rectangle({self.width}x{self.height})'
#
#
# r = Rectangle(3, 4)
# e = Rectangle(2, 5)
# q = r + e
# print(q)
#


# class Order:
#     def __init__(self, cart, customer):
#         self.cart = cart
#         self.customer = customer
#
#     def __add__(self, other):
#         return Order(self.cart + [other], self.customer)
#
#     def __radd__(self, other):
#         return Order([other] + self.cart, self.customer)
#
#     def __sub__(self, other):
#         if other in self.cart:
#             self.cart.remove(other)
#         return Order(self.cart, self.customer)
#
#     def __rsub__(self, other):
#         if other in self.cart:
#             self.cart.remove(other)
#         return Order(self.cart, self.customer)
#
#
# order = Order(['banana', 'apple'], 'Гена Букин')
#
# order_2 = order + 'orange'
# assert order.cart == ['banana', 'apple']
# assert order.customer == 'Гена Букин'
# assert order_2.cart == ['banana', 'apple', 'orange']
#
# order = 'mango' + order
# assert order.cart == ['mango', 'banana', 'apple']
# order = 'ice cream' + order
# assert order.cart == ['ice cream', 'mango', 'banana', 'apple']
#
# order = order - 'banana'
# assert order.cart == ['ice cream', 'mango', 'apple']
#
# order3 = order - 'banana'
# assert order3.cart == ['ice cream', 'mango', 'apple']
#
# order = order - 'mango'
# assert order.cart == ['ice cream', 'apple']
# order = 'lime' - order
# assert order.cart == ['ice cream', 'apple']
# print('Good')
# def test(*args):
#     value = [num for num in args if type(num) == int]
#     return sorted(value)
#
#
# print(test('dweed', 3.4))
#
#
# class Vector:
#     def __init__(self, *args):
#         self.values = sorted([num for num in args if type(num) == int])
#
#     def __str__(self):
#         if len(self.values) > 0:
#             return f"Вектор{sorted(tuple(self.values))}"
#         return "Пустой вектор"
#
#     def __add__(self, other):
#         if isinstance(other, int):
#             for i in range(len(self.values)):
#                 self.values[i] += other
#             return Vector(sorted(self.values))
#
#
# tes = Vector(3, 2)
# tes + 2
# print(tes)
# class Vector:
#     def __init__(self, *args):
#         self.values = sorted([num for num in args if type(num) == int])
#
#     def __str__(self):
#         if len(self.values):
#             return f"Вектор{tuple(sorted(self.values))}"
#         return "Пустой вектор"
#
#     def __add__(self, other):
#         if isinstance(other, int):
#             new_lst = [i + other for i in self.values]
#             return Vector(*new_lst)
#         elif isinstance(other, Vector):
#             if len(other.values) == len(self.values):
#                 lst = [x + y for x, y in zip(self.values, other.values)]
#                 return Vector(*lst)
#             elif len(other.values) != len(self.values):
#                 print("Сложение векторов разной длины недопустимо")
#         else:
#             print(f'Вектор нельзя сложить с {other}')
#
#     def __mul__(self, other):
#         if isinstance(other, int):
#             new_vector = [i * other for i in self.values]
#             return Vector(*new_vector)
#
#         elif isinstance(other, Vector):
#             if len(other.values) == len(self.values):
#                 new_vector = [x * y for x, y in zip(self.values, other.values)]
#                 return Vector(*new_vector)
#             else:
#                 print("Умножение векторов разной длины недопустимо")
#         else:
#             print(f"Вектор нельзя умножать с {other}")
#
#
# v1 = Vector(1, 2, 3)
# print(v1)  # печатает "Вектор(1, 2, 3)"
#
# v2 = Vector(3, 4, 5)
# print(v2)  # печатает "Вектор(3, 4, 5)"
# v3 = v1 + v2
# print(v3)  # печатает "Вектор(4, 6, 8)"
# v4 = v3 + 5
# print(v4) # печатает "Вектор(9, 11, 13)"
# v5 = v1 * 2
# print(v5) # печатает "Вектор(2, 4, 6)"
# v5 + 'hi' # печатает "Вектор нельзя сложить с hi"
# def print_products(*args):
#     products = [elem for elem in args if type(elem) == str]
#     if len(products):
#         for i, product in enumerate(products, 1):
#             print(f'{i}) {product}')
#     else:
#         print('Нет продуктов')
#
# print_products(323,[32,32],'ewewe','dscsc')
# Напишите определение класса Rectangle
# from functools import total_ordering
#
#
# @total_ordering
# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     @property
#     def area(self):
#         return self.height * self.width
#
#     def __eq__(self, other):
#         if isinstance(other, (int, float)):
#             return self.width == other or self.height == other or self.area == other
#         elif isinstance(other, Rectangle):
#             return self.area == other.area
#
#     def __lt__(self, other):
#         if isinstance(other, (int, float)):
#             return self.area < other
#         elif isinstance(other, Rectangle):
#             return self.area < other.area
#
#
# # Ниже код для проверки методов класса Rectangle
#
# r1 = Rectangle(3, 4)
# assert r1.width == 3
# assert r1.height == 4
# assert r1.area == 12
# assert isinstance(type(r1).area, property), 'Вы не создали property area'
#
# assert r1 > 11
# assert not r1 > 12
# assert r1 >= 12
# assert r1 <= 12
# assert not r1 > 13
# assert not r1 == 13
# assert r1 != 13
# assert r1 == 12
#
# r2 = Rectangle(2, 6)
# assert r1 == r2
# assert not r1 != r2
# assert not r1 > r2
# assert not r1 < r2
# assert r1 >= r2
# assert r1 <= r2
#
# r3 = Rectangle(5, 2)
# assert not r2 == r3
# assert r2 != r3
# assert r2 > r3
# assert not r2 < r3
# assert r2 >= r3
# assert not r2 <= r3
# print('Good')
# class Quadrilateral:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def __str__(self):
#         if self.width == self.height:
#             return f'Квадрат размером {self.width}х{self.height}'
#         return f'Прямоугольник размером {self.width}х{self.height}'
#
#     def __bool__(self):
#         return self.width == self.height
#
#
# a = Quadrilateral(3, 4)
# print(callable(a))
# import time
#
#
# class Timer:
#     def __init__(self, func):
#         self.fn = func
#
#     def __call__(self, *args, **kwargs):
#         start = time.time()
#         result = self.fn(*args, *kwargs)
#         finish = time.time()
#         print(finish - start)
#         return result
#
#
# @Timer
# def calculate():
#     for i in range(10000000):
#         2 ** 100
#
#
# print(calculate())
# class Rectangle:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def __str__(self):
#         return f'Прямоугольник {self.a}x{self.b}'
#
#     def get_area(self):
#         return self.a * self.b
#
#
# class Sq:
#     def __init__(self, a):
#         self.a = a
#
#     def __str__(self):
#         return f'Квадрат {self.a}x{self.a}'
#
#     def get_area(self):
#         return self.a ** 2
#
#
# class Cir:
#     def __init__(self, r):
#         self.r = r
#
#     def __repr__(self):
#         return f'ky'
#
#     def __str__(self):
#         return f'Круг Радиусом {self.r}'
#
#     def get_area(self, ):
#         return 3.14 * self.r ** 2
#
#
# c = Rectangle(3, 5)
# d = Sq(2)
# e = Cir(7)
#
# figures = [c, d, e]
# for figure in figures:
#     print(figure, figure.get_area())
# class Cat:
#     def __init__(self, name):
#         self.name = name
#
#     def info(self):
#         print(f"I am a cat. My name is {self.name}.")
#
#     def make_sound(self):
#         print("Meow")
#
#
# class Dog:
#     def __init__(self, name):
#         self.name = name
#
#     def info(self):
#         print(f"I am a dog. My name is {self.name}.")
#
#     def make_sound(self):
#         print("Bark")
#
#
# cat_obj = Cat("Ren")
# dog_obj = Dog("Stimpy")
#
# for animal in (cat_obj, dog_obj):
#     animal.make_sound()
#     animal.info()
#     animal.make_sound()
# class Building:
#     def __init__(self, floors):
#         self.floors = list([None] * floors)
#
#     def __setitem__(self, key, values):
#         if 0 <= key < len(self.floors):
#             self.floors[key] = values
#             return self.floors
#         raise IndexError
#
#     def __getitem__(self, key):
#         if 0 <= key < len(self.floors):
#             return self.floors[key]
#
#     def __delitem__(self, key):
#         if 0 <= key < len(self.floors):
#             self.floors[key] = None
#
#
# iron_building = Building(22)  # Создаем здание с 22 этажами
# iron_building[0] = 'Reception'
# iron_building[1] = 'Oscorp Industries'
# iron_building[2] = 'Stark Industries'
# print(iron_building[2])
# del iron_building[2]
# print(iron_building[2])
# iron_building[3] = 'dfd'
# print(iron_building[3])
# iron_building[3] = 'trtr'
# print(iron_building[3])
# print(iron_building.floors)
# class ShoppingCart:
#     def __init__(self):
#         self.items = {}
#
#     def __getitem__(self, key):
#         return self.items.get(key, 0)
#
#     def __setitem__(self, key, value):
#         self.items[key] = value
#
#     def __delitem__(self, key):
#         del self.items[key]
#
#     def add_item(self, key, value=1):
#         self.items[key] = self.items.get(key, 0) + value
#
#     def remove_item(self, key, value=1):
#         if key not in self.items.keys():
#             return f'There is no a such item'
#         elif value >= self.items[key]:
#             del self.items[key]
#         else:
#             self.items[key] = self.items[key] - value
#
#
# cart = ShoppingCart()
#
# # Add some items to the cart
# cart.add_item('Apple', 3)
# cart.add_item('Banana', 2)
# cart.add_item('Orange')
#
# assert cart['Banana'] == 2
# assert cart['Orange'] == 1
# assert cart['Kivi'] == 0
#
# cart.add_item('Orange', 9)
# assert cart['Orange'] == 10
#
# print("Shopping Cart:")
# for item_name in cart.items:
#     print(f"{item_name}: {cart[item_name]}")
#
# cart['Apple'] = 5
# cart['Banana'] = 7
# cart['Kivi'] = 11
# assert cart['Apple'] == 5
# assert cart['Banana'] == 7
# assert cart['Kivi'] == 11
#
# print("Updated Shopping Cart:")
# for item_name in cart.items:
#     print(f"{item_name}: {cart[item_name]}")
#
# # Remove an item from the cart
# cart.remove_item('Banana')
# assert cart['Banana'] == 6
#
# cart.remove_item('Apple', 4)
# assert cart['Apple'] == 1
#
# cart.remove_item('Apple', 2)
# assert cart['Apple'] == 0
# assert 'Apple' not in cart.items
#
# cart.remove_item('Potato')
#
# del cart['Banana']
# assert cart['Banana'] == 0
# assert 'Banana' not in cart.items
#
# print("Updated Shopping Cart:")
# for item_name in cart.items:
#     print(f"{item_name}: {cart[item_name]}")
# class NewInt(int):
#     def __init__(self, num):
#         self.num = num
#
#     def repeat(self, n=2):
#         return int(str(self.num) * n)
#
#     def to_bin(self):
#         return int(f'{self.num:b}')
#
#
# a = NewInt(9)
# print(a.repeat())  # печатает число 99
# d = NewInt(a + 5)
# print(d.repeat(3))  # печатает число 141414
# b = NewInt(NewInt(7) * NewInt(5))
# print(b.to_bin())
# class Vehicle:
#
#     def __init__(self, name= 'dfd', mileage=3434, capacity=80):
#         self.name = name
#         self.mileage = mileage
#         self.capacity = capacity
#
#     def fare(self):
#         return self.capacity * 100
#
#     def display(self):
#         print(f'Total {self.name} fare is: {self.fare()}')
#
#
# class Bus(Vehicle):
#
#     def __init__(self, name, mileage, capacity=50):
#         super().__init__(name, mileage, capacity)
#
#     def fare(self):
#         return (self.capacity * 100) * 1.1
#
#
# class Taxi(Vehicle):
#
#     def __init__(self, name, mileage, capacity=4):
#         super().__init__(name, mileage, capacity)
#
#     def fare(self):
#         return (self.capacity * 1.35) * 100
#
#
# sc = Vehicle('Scooter', 100, 2)
# sc.display()
#
# merc = Bus("Mercedes", 120000)
# merc.display()
#
# polo = Taxi("Volkswagen Polo", 15000)
# polo.display()
# class Transport:
#     def __init__(self, brand, max_speed, kind=None):
#         self.brand = brand
#         self.max_speed = max_speed
#         self.kind = kind
#
#     def __str__(self):
#         return f"Тип транспорта {self.kind} марки {self.brand} может развить скорость {self.max_speed} км/ч"
#
#
# class Car(Transport):
#     def __init__(self, brand, max_speed, mileage, gasoline_residue):
#         super().__init__(brand, max_speed, kind='Car')
#         self.mileage = mileage
#         self._gasoline_residue = gasoline_residue
#
#     @property
#     def gasoline(self):
#         return f"Осталось бензина на {self._gasoline_residue} км"
#
#     @gasoline.setter
#     def gasoline(self, value):
#         if isinstance(value, int):
#             self._gasoline_residue += value
#             print(f'Объем топлива увеличен на {value} л и составляет {self._gasoline_residue} л')
#         else:
#             print('Ошибка заправки автомобиля')
#
#
# class Boat(Transport):
#     def __init__(self, brand, max_speed, owners_name):
#         super().__init__(brand, max_speed, kind='Boat')
#         self.owners_name = owners_name
#
#     def __str__(self):
#         return f'Этой лодкой марки {self.brand} владеет {self.owners_name}'
#
#
# class Plane(Transport):
#     def __init__(self, brand, max_speed, capacity):
#         super().__init__(brand, max_speed, kind='Plane')
#         self.capacity = capacity
#
#     def __str__(self):
#         return f'Самолет марки {self.brand} вмещает в себя {self.capacity} людей'
#
#
# transport = Transport('Telega', 10)
# print(transport)  # Тип транспорта None марки Telega может развить скорость 10 км/ч
# bike = Transport('shkolnik', 20, 'bike')
# print(bike)  # Тип транспорта bike марки shkolnik может развить скорость 20 км/ч
#
# first_plane = Plane('Virgin Atlantic', 700, 450)
# print(first_plane)  # Самолет марки Virgin Atlantic вмещает в себя 450 людей
# first_car = Car('BMW', 230, 75000, 300)
# print(first_car)  # Тип транспорта Car марки BMW может развить скорость 230 км/ч
# print(first_car.gasoline)  # Осталось бензина на 300 км
# first_car.gasoline = 20  # Печатает 'Объем топлива увеличен на 20 л и составляет 320 л'
# print(first_car.gasoline)  # Осталось бензина на 320 км
# second_car = Car('Audi', 230, 70000, 130)
# second_car.gasoline = [None]  # Печатает 'Ошибка заправки автомобиля'
# first_boat = Boat('Yamaha', 40, 'Petr')
# print(first_boat)  # Этой лодкой марки Yamaha владеет Petr
# from functools import total_ordering
#
#
# class Initialization:
#     def __init__(self, capacity, food):
#         if not isinstance(capacity, int):
#             print('Количество людей должно быть целым числом')
#         else:
#             self.capacity = capacity
#             self.food = food
#
#
# class Vegetarian(Initialization):
#     def __init__(self, capacity, food):
#         super().__init__(capacity, food)
#
#     def __str__(self):
#         return f"{self.capacity} людей предпочитают не есть мясо! Они предпочитают {self.food}"
#
#
# class MeatEater(Initialization):
#     def __init__(self, capacity, food):
#         super().__init__(capacity, food)
#
#     def __str__(self):
#         return f"{self.capacity} мясоедов в Москве! Помимо мяса они едят еще и {self.food}"
#
#
# @total_ordering
# class SweetTooth(Initialization):
#     def __init__(self, capacity, food):
#         super().__init__(capacity, food)
#
#     def __str__(self):
#         return f'Сладкоежек в Москве {self.capacity}. Их самая любимая еда: {self.food}'
#
#     def __eq__(self, other):
#         if isinstance(other, int):
#             return self.capacity == other
#         elif isinstance(other, Initialization):
#             return self.capacity == other.capacity
#         else:
#             return f'Невозможно сравнить количество сладкоежек с {other}'
#
#     def __lt__(self, other):
#         if isinstance(other, int):
#             return self.capacity < other
#         elif isinstance(other, (Vegetarian, MeatEater)):
#             return self.capacity < other.capacity
#         else:
#             return f'Невозможно сравнить количество сладкоежек с {other}'
#
#
# v_first = Vegetarian(10000, ['Орехи', 'овощи', 'фрукты'])
# print(v_first)  # 10000 людей предпочитают не есть мясо! Они предпочитают ['Орехи', 'овощи', 'фрукты']
# v_second = Vegetarian([23], ['nothing'])  # Количество людей должно быть целым числом
# m_first = MeatEater(15000, ['Жареную картошку', 'рыба'])
# print(m_first)  # 15000 мясоедов в Москве! Помимо мяса они едят еще и ['Жареную картошку', 'рыба']
# s_first = SweetTooth(30000, ['Мороженое', 'Чипсы', 'ШОКОЛАД'])
# print(s_first)  # Сладкоежек в Москве 30000. Их самая любимая еда: ['Мороженое', 'Чипсы', 'ШОКОЛАД']
# print(s_first > v_first)  # True
# print(30000 == s_first)  # True
# print(s_first == 25000)  # False
# print(100000 < s_first)  # False
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
#
#     def __init__(self, company_name, location):
#         self.company_name = company_name
#         self.location = location
#
#     def display_company_info(self):
#         print(f'Company: {self.company_name}, {self.location}')
#
#
# class Employee(Person, Company):
#
#     def __init__(self, name, age, company_name, location):
#         super().__init__(name, age)
#         Company.__init__(self, company_name, location)
#
#
# emp = Employee('Jessica', 28, 'Google', 'Atlanta')
# emp.display_person_info()
# emp.display_company_info()
# class Animal:
#     def __init__(self, name, species):
#         self.name = name
#         self.species = species
#
#     def eat(self):
#         print(f'{self.name} is eating.')
#
#     def sleep(self):
#         print(f'{self.name} is sleeping.')
#
#
# class Dog(Animal):
#     def __init__(self, name, breed, species):
#         super().__init__(name, species)
#         self.breed = breed
#
#     def bark(self):
#         print('Woof!')
#
#
# class Cat(Animal):
#     def __init__(self, name, color):
#         super().__init__(name, 'cat')
#         self.color = color
#
#     def meow(self):
#         print('Meow!')
#
#
# bars = Cat('Bars','brown')
# print(bars.__dict__)
# class BasePizza:
#     BASE_PIZZA_PRICE = 15
#
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#         self.toppings = ['cheese']
#
#     def __str__(self):
#         return f"{self.name} with {self.toppings}, ${self.price:.2f}"
#
#
# class PepperoniMixin:
#     def add_pepperoni(self):
#         print("Adding pepperoni!")
#         self.price += 5
#         self.toppings += ['pepperoni']
#
#
# class MushroomMixin:
#     def add_mushrooms(self):
#         print("Adding mushrooms!")
#         self.price += 3
#         self.toppings += ['mushrooms']
#
#
# class OnionMixin:
#     def add_onion(self):
#         print("Adding onion!")
#         self.price += 2
#         self.toppings += ['onion']
#
#
# class BaconMixin:
#     def add_bacon(self):
#         print("Adding bacon!")
#         self.price += 6
#         self.toppings += ['bacon']
#
#
# class OlivesMixin:
#     def add_olives(self):
#         print("Adding olives!")
#         self.price += 1
#         self.toppings += ['olives']
#
#
# class HamMixin:
#     def add_ham(self):
#         print('Adding ham')
#         self.price += 7
#         self.toppings += ['ham']
#
#
# class PepperMixin:
#     def add_pepper(self):
#         print('Adding pepper')
#         self.price += 3
#         self.toppings += ['pepper']
#
#
# class ChickenMixin:
#     def add_chicken(self):
#         print('Adding chicken')
#         self.price += 5
#         self.toppings += ['chicken']
#
#
# class OlivesPizza(BasePizza, OlivesMixin):
#
#     def __init__(self):
#         super().__init__('Море оливок', BasePizza.BASE_PIZZA_PRICE)
#         self.add_olives()
#
#
# class PepperoniPizza(BasePizza, PepperoniMixin):
#
#     def __init__(self):
#         super().__init__('Колбасятина', BasePizza.BASE_PIZZA_PRICE)
#         self.add_pepperoni()
#
#
# class MushroomOnionBaconPizza(BasePizza, MushroomMixin, OnionMixin, BaconMixin):
#
#     def __init__(self):
#         super().__init__('Грибной пяточок с луком', BasePizza.BASE_PIZZA_PRICE)
#         self.add_mushrooms()
#         self.add_onion()
#         self.add_bacon()
#
#
# # Создайте экземпляр CountryPizza в переменной pizza
# class CountryPizza(BasePizza, HamMixin, PepperMixin, OlivesMixin, PepperoniMixin, MushroomMixin, ChickenMixin):
#
#     def __init__(self):
#         super().__init__('Деревенская пицца', BasePizza.BASE_PIZZA_PRICE)
#         self.add_ham()
#         self.add_pepper()
#         self.add_olives()
#         self.add_pepperoni()
#         self.add_mushrooms()
#         self.add_chicken()
#
#
# pizza = CountryPizza()
#
# # Код для проверки
#
# assert pizza.name == 'Деревенская пицца'
# assert pizza.price == 39
# assert pizza.toppings == ['cheese', 'ham', 'pepper', 'olives', 'pepperoni', 'mushrooms', 'chicken']
# print(pizza)
print(10)



