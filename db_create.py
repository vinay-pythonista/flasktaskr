# db_create.py


from project import db
#from project.models import Task, User
#from datetime import date


# create the database and the db table
db.create_all()

#db.session.add(User("admin", "ad@min.com", "admin", "admin"))
#db.session.add(Task("Finish this tutorial", date(2016, 9, 22), 10, date(2015, 2, 13), 1, 1))
#db.session.add(Task("Finish Real Python", date(2016, 10, 3), 10, date(2015, 2, 13), 1, 1))

db.session.commit()