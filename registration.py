from user import User

jane = User("Bingham University","Karu, Nasarawa")
jane.show()

user = User("Bingham University", "Karu, Nasarawa")
user.register("james", "111", "abc","abc")

email = input("Enter Email: ")

password = input("Enter Password: ")
print(user.login(email, password))
