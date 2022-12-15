class People:
    name = ""
    _gender = ""  # protected because using _
    __age = 0  # private because using __

    def __init__(self) -> None:
        pass

    def __init__(self, name):
        self.name = name

    def __init__(self, name, gender="M", age=0):
        self.name = name
        self._gender = gender
        self.__age = age

    def setname(self, name):
        self.name = name

    def setgender(self, gender):
        self._gender = gender

    def setage(self, age):
        self.__age = age

    def getage(self):
        return self.__age


p1 = People("Alex", "F", 20)
# p1 = People("Bin")
# p1 = People

# raise an AtrributeError, "__age" only accessible within the class
# print(f"{p1.name} has gender {p1._gender}. and now {p1.__age}")

print(f"{p1.name} has gender {p1._gender}.")

p1.setage(60)
print(f"{p1.name} has gender {p1._gender}.and now {p1.getage()}")
