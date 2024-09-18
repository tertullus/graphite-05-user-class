class UserClass:
    def __init__(self, name, age, location):
        self.__name = name
        self.__age = age
        self.__location = location

    def view_user_data(self):
        print("User's name:", self.__name)
        print("User's age:", self.__age)
        print("User's location:", self.__location)
        print("--------------------------------------")

    def change_user_data(self):
        self.__name = input("Change the user's name: ")
        self.__age = input("Change the user's age: ")
        self.__location = input("Change the user's location: ")
        print("--------------------------------------")


user_01 = UserClass("Chideraa", 23, "Sangotedo")
user_01.view_user_data()
user_01.change_user_data()
user_01.view_user_data()

user_02 = UserClass("Ebenezer", 24, "Enugu")
user_02.view_user_data()
user_02.change_user_data()
user_02.view_user_data()

user_03 = UserClass("Tertullus", 40, "Cilicia")
user_03.view_user_data()
user_03.change_user_data()
user_03.view_user_data()
