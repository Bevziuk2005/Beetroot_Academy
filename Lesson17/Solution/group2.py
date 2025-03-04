import json

class User:
    def __init__(self, username, filename="database.json"):
        self.username = username
        self.filename = filename
    def inf(self):
        raise Exception("You are not user")

    def create_post(self, content):
        data = self.read()
        data.append({"username": self.username, "content": content})

        with open(self.filename, "w") as file:
            json.dump(data, file)

    def available_actions(self):
        print("Available actions:")
        print("1. Create Post")
        print("2. View Profile")

        choice = int(input("Enter you choice: "))

        if choice == 1:
            content = input("Enter content: ")
            self.create_post(content)
        elif choice == 2:
            self.inf()
        else:
            print("Invalid choice. Please enter one of the above numbers.")

    def write(self, data):
        with open(self.filename, "w") as file:
            json.dump(data, file)

    def read(self):
        try:
            with open(self.filename, "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            data = []

        return data

class RegularUser(User):
    def __init__(self, username):
        print("Welcome Regular User!")
        super().__init__(username)

    def inf(self):
        print("You information:")
        print(self.username)
        for i, j in enumerate(self.read()):
            print(i, j)

class AdminUser(User):
    def __init__(self, username):
        print("Welcome Regular User!")
        super().__init__(username)

    print("Available actions:")
    print("1. Create Post")
    print("2. View Profile")
    print("3. Delete post")

    choice = int(input("Enter you choice: "))

    if choice == 1:
        content = input("Enter content: ")
        self.create_post(content)
    elif choice == 2:
        self.inf()
    elif choice == 3:
        data = self.read()
        for post in data:
            self.del_post(post)

    def inf(self):
        print("You information:")
        print(self.username)
        for i, j in enumerate(self.read()):
            print(i, j)

    def change_post(self):
        print("Available actions:")
        print("1. Create Post")
        print("2. View Profile")

        choice = int(input("Enter you choice: "))

        if choice == 1:
            content = input("Enter content: ")
            self.create_post(content)
        elif choice == 2:
            self.inf()
        else:
            print("Invalid choice. Please enter one of the above numbers.")

    def del_post(self):
        if self.__class__.__name__ == "Admin":
            data = self.read()

            for item in data:
                if item == post:
                    data.remove(item)
                    self.write(data)
                    print("Post deleted")
                print("Post not found")
            else:
                print("You do not have permission")

class PremiumUser(User):
    def __init__(self, username):
        print("Welcome Regular User!")
        print("Youre function:\n")
        super().__init__(username)


    def inf(self):
        print("You information:")
        print(self.username)
        for i, j in enumerate(self.read()):
            print(i, j)


    def copy_post(self):







#           TEST
user1 = User("test")
user1.available_actions()



