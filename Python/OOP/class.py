class User:

    def __init__(self, username, user_id):
        self.name = username
        self.id = user_id
        self.followers = 0
        self.following = 0
    
    def follow(self, user):
        user.followers+=1
        self.following+= 1

user1 = User("Kiran", 9)
user2 = User("Ishan", 5)
# user1.username = "Kiran"
# user1.id = 1


user1.follow(user2)
print(user1.following)
print(user1.followers)
print(user2.followers)
print(user2.following)


