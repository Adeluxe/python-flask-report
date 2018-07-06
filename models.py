from project import db
from werkzeug.security import generate_password_hash, check_password_hash

class UserModel(db.Model):
	__tablename__ = 'users'

	eid = db.Column(db.String(20), primary_key = True)
	name = db.Column(db.String(80))
	email = db.Column(db.String(80), unique = True)
	password_hash = db.Column(db.String(128))

	def __init__(self, eid, name, email, password):
		self.eid = eid
		self.name = name
		self.email = email
		self.password_hash = generate_password_hash(password)

	def check_password(self, password):
		return check_password_hash(self.password_hash, password)

	@classmethod
	def find_by_eid(cls, eid):
		return cls.query.filter_by(eid=eid).first()

	def save_to_db(self):
		db.session.add(self)
		db.session.commit()

	def delete_from_db(self):
		db.session.delete(self)
		db.session.commit()

	def __repr__(self):
		return "The user is {} (eid is {}) and email is {}".format(self.name, self.eid, self.email)
