# Задание 7: Использование объектно-ориентированной парадигмы 
# Создайте класс User и его наследника класс SuperUser, 
# которые описывают пользователя и супер-пользователя.   
# В классе User необходимо описать: конструктор, который 
# принимает в качестве параметров значения для атрибутов name, 
# login и password свойства для изменения и получения значений 
# атрибутов метод show_info, который печатает в произвольном 
# формате значения атрибутов name и login атрибут класса count 
# для хранения количества созданных экземпляров класса User 
# Необходимые условия, которые надо учесть: атрибут name
# доступен и для чтения, и для изменения атрибут login доступен 
# только для чтения атрибут password доступен только для 
# изменения   В классе SuperUser необходимо описать: 
# конструктор, который принимает в качестве параметров 
# значения для атрибутов name, login, password и role свойство 
# для изменения и получения значения атрибута role 
# метод show_info, который печатает в произвольном формате 
# значения атрибутов name, login и role атрибут класса count 
# для хранения количества созданных экземпляров 
# класса SuperUser   Как это должно работать   
# user1 = User('Paul McCartney', 'paul', '1234') 
# user2 = User('George Harrison', 'george', '5678') 
# user3 = User('Richard Starkey', 'ringo', '8523') 
# admin = SuperUser('John Lennon', 'john', '0000', 'admin') 
# user1.show_info() admin.show_info()   Name: Paul McCartney, 
# Login: paul Name: John Lennon, Login: john   
# users = User.count admins = SuperUser.count 
# print(f'Всего обычных пользователей: {users}') 
# print(f'Всего супер-пользователей: {admins}')   
# Всего обычных пользователей: 3 
# Всего супер-пользователей: 1   
# user3.name = 'Ringo Star' 
# user1.password = 'Pa$$w0rd' print(user3.name) 
# print(user2.password) print(user2.login) 
# user2.login = 'geo'   
# Ringo Starr ******** george AttributeError: 
# can't set attribute

class User:
    count = 0

    def __init__(self, name, login, password):
        self._name = name
        self._login = login
        self._password = password
        User.count += 1

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    @property
    def login(self):
        return self._login

    @property
    def password(self):
        return "********"

    @password.setter
    def password(self, new_password):
        self._password = new_password

    def show_info(self):
        print(f"Name: {self.name}, Login: {self.login}")


class SuperUser(User):
    count = 0

    def __init__(self, name, login, password, role):
        super().__init__(name, login, password)
        self._role = role
        SuperUser.count += 1

    @property
    def role(self):
        return self._role

    @role.setter
    def role(self, new_role):
        self._role = new_role

    def show_info(self):
        print(f"Name: {self.name}, Login: {self.login}, Role: {self.role}")


user1 = User('Paul McCartney', 'paul', '1234')
user2 = User('George Harrison', 'george', '5678')
user3 = User('Richard Starkey', 'ringo', '8523')
admin = SuperUser('Maria Nikonets', 'maria', '0000', 'admin')

user1.show_info()
admin.show_info()

print(f'Всего обычных пользователей: {User.count}')
print(f'Всего супер-пользователей: {SuperUser.count}')

user3.name = 'Ringo Starr'
user1.password = 'Pa$$w0rd'
print(user3.name)
print(user1.password)
print(user2.login)


