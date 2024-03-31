# Разработай систему управления учетными записями пользователей для небольшой компании.
# Компания разделяет сотрудников на обычных работников и администраторов.
# У каждого сотрудника есть уникальный идентификатор (ID), имя и уровень доступа.
# Администраторы, помимо обычных данных пользователей, имеют дополнительный уровень доступа
# и могут добавлять или удалять пользователя из системы.
#
# Требования:
# 1.Класс `User*: Этот класс должен инкапсулировать данные о пользователе: ID, имя и уровень доступа
# ('user' для обычных сотрудников).

# 2.Класс Admin: Этот класс должен наследоваться от класса User.
# Добавь дополнительный атрибут уровня доступа, специфичный для администраторов ('admin').
# Класс должен также содержать методы add_user и remove_user, которые позволяют добавлять и удалять пользователей
# из списка (представь, что это просто список экземпляров User).
#
# 3.Инкапсуляция данных: Убедись, что атрибуты классов защищены от прямого доступа и модификации снаружи.
# Предоставь доступ к необходимым атрибутам через методы (например, get и set методы).

# Определение базового класса User
class User:
    def __init__(self, user_id, name):
        self.__user_id = user_id
        self.__name = name
        self.__access_level = 'user'

    # Геттеры и сеттеры для атрибутов класса
    @property
    def user_id(self):
        return self.__user_id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def access_level(self):
        return self.__access_level

# Расширение класса User классом Admin
class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name)
        self.__access_level = 'admin'
        self.__users = []  # Список для хранения учетных записей пользователей

    @property
    def access_level(self):
        return self.__access_level

    # Метод для добавления пользователя
    def add_user(self, user):
        if user not in self.__users:
            self.__users.append(user)
            print(f"Пользователь {user.name} добавлен.")
        else:
            print("Пользователь уже существует.")

    # Метод для удаления пользователя
    def remove_user(self, user):
        if user in self.__users:
            self.__users.remove(user)
            print(f"Пользователь {user.name} удален.")
        else:
            print("Пользователь не найден.")

    # Метод для отображения списка пользователей
    def list_users(self):
        print("Список пользователей:")
        for user in self.__users:
            print(f"- ID: {user.user_id}, Имя: {user.name}, Уровень доступа: {user.access_level}")

# Пример использования
admin = Admin(1, 'Администратор Иван')
user1 = User(2, 'Пользователь Петр')
user2 = User(3, 'Пользователь Анастасия')

admin.add_user(user1)
admin.add_user(user2)
admin.list_users()

admin.remove_user(user1)
admin.list_users()
