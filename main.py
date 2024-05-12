class User():
    def __init__(self, id, name):  # атрибуты класса: id, имя
        self.public_id = id  # открытый атрибут
        self._protected_name = name  #  защищенный атрибут
        self.__private_level = 'user'  # приватный атрибут

    def public_method(self):
        return f'Это открытый метод. Номер работника: {self.public_id} {self._protected_name}.'

    def _protected_method(self):
        return f'Это защищенный метод. Имя работника: {self._protected_name}.'

    def __private_method(self):
        return f'Это приватный метод. Уровень работника: {self.__private_level}.'


class Admin(User):
    def __init__(self, id, name, admin):
        super().__init__(id, name)
        self.admin = admin
        self.users_list = []

    def get_private(self): # функция для доступа к информации
        return self.__private

    def set_private(self):  # функция для изменения информации
        self.__private

    def add_user(self, user_id, name, admin): #функция добавления работника
        new_user = User(user_id, name)
        self.users_list.append(new_user)
        print(f'{name} работник добавлен.')


    def remove_user(self, user_id): # Удаление работника
        for user in self.users_list:
            if user.user_id == user_id:
                self.users_list.remove(user)
                print(f'{user.name} - работник удален.')
                return
        print(f'{user_id} такого работника нет.')

    def get_info(self):
        info = f"{self.public_id} {self._protected_name} Уровень: {self.admin}."
        return info

admin = Admin(1, 'Иван', 'admin')  # экземпляр
admin_1 = Admin(2, 'Саша', 'user')
admin_2 = Admin(3, 'Вася', 'user')
admin.remove_user(2)
admin_2.add_user(5, 'Оля', 'user')