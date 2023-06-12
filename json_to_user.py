class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

user = {
    "name": "John Doe",
    "email": "johndoe@gmail.com",
    "password": "password123"
}

#TODO: write a function that takes in a json and returns a User class
def create_user(json):

#TODO: create a function that takes in a User class and returns a json
def jsonify_user(user):
