# working with constructor
class User:
    def __init__(self,user_id,username):
        self.id=user_id
        self.username=username
        # a parameter can also be provided with a default value & it doesnt need to be in initializer (init)
        self.follower=0

# creating objects with defined attributes
user_1=User("001","IshY")
user_2=User("002","Sands")

print(user_2.id)
print(user_2.username)
print(user_1.follower)

