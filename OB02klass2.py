class Test():
    def public_func(self):
        print("Это публичный метод")

    def _protected_func(self):
        print("Это защищенный метод")

    def __private_func(self):
        print("Это приватный метод")
    def test_private_func(self):
        self.__private_func()


test = Test()
test.public_func()
test._protected_func()

test.test_private_func()