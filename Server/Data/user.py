import mongoengine

class User(mongoengine.Document):
    name = mongoengine.StringField(required=True)
    email = mongoengine.StringField(required=True)


    expenses_ids = mongoengine.ListField()