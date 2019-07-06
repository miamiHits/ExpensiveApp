from Infrastructure import mongo_init, data_services
import mongoengine

if __name__ == '__main__':
    alias_db = "default"
    db_name = "expenses"

    mongo_init.create_db(alias_db, db_name)
    print("DB {} was created!".format(db_name))

    name = input("Please enter your name ")
    email = input("Please enter your mail ").strip().lower()

    if data_services.is_acount_exist_by_email(email):
        print("Acount Exsist")

    else:
        data_services.create_acount(name, email)
        print("Acount was created")

