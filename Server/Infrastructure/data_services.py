from Data.user import User

def create_acount(name: str, email: str) -> User:
    user = User()
    user.name = name
    user.email = email

    user.save()

    return user

def is_acount_exist_by_email(email: str) -> bool:
    if None is User.objects(email=email).first():
        return False

    return True