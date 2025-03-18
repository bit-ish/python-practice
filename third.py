class User:
    def __init__(self,user_id,username):
        self.id=user_id
        self.username=username

        self.follower=0
        self.following=0
    # defining method
    def follow(self,user):
        user.follower+=1
        self.following+=1

user_1=User("001","IshY")
user_2=User("002","Sands")

user_1.follow(user_2)

print(f"{user_1.follower}\n{user_1.following}\n{user_2.follower}\n{user_2.following}")


