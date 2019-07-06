import mongoengine

def create_db(alias_db, db_name):
    mongoengine.register_connection(alias = alias_db, name = db_name)


