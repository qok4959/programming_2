class UserAuth:

    def __init__(self, users):
        self.users=users


    def login(self, username, password):
        if username in self.users and self.users[username]==password:
            print("Suckes")
        elif username not in self.users:
            raise UserNotFoundError(f"username={username} not found, try different username")
        elif username in self.users and self.users[username]!=password:
            raise WrongPasswordError(f"Password for username={username} is incorrect")



class UserNotFoundError(Exception):
    pass

class WrongPasswordError(RuntimeError):
    pass


auth = UserAuth({"admin": "1234", "user":"abcd"})

for username, password in [("admin", "1234"), ("user", "wrongpass"), ("Unknown", "pass")]:
    try:
        auth.login(username, password)
    except UserNotFoundError as e:
        print(f"UserNotFoundError: {e}")
    except WrongPasswordError as e:
        print(f"WrongPasswordError: {e}")
    except Exception as e:
        print(f"Blad, {e}")