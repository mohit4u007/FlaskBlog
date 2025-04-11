# This script creates the database and tables for the Flask application
import json
from flaskblog.models import Post, User
from flaskblog import db, bcrypt, create_app

app = create_app()

if __name__ == '__main__':
	with app.app_context():
		# Create the database and tables
		db.create_all()
		# Create two users as the sample dummy data uses two users
		hashed_password = bcrypt.generate_password_hash('mypass').decode('utf-8')
		user1 = User(username='MohitKS', email='mohit4u007@gmail.com', password=hashed_password)
		db.session.add(user1)
		db.session.commit()

		hashed_password = bcrypt.generate_password_hash('mypass').decode('utf-8')
		user2 = User(username='NewUser', email='NewUser@mail.com', password=hashed_password)
		db.session.add(user2)
		db.session.commit()
		# Following code will create dummy posts belonging to two users created above
		with open('posts.json', 'r') as f:
			posts = json.load(f)

			for post in posts:
				new_post = Post(title=post['title'], content=post['content'], author=user1 if post['user_id']==1 else user2)
				db.session.add(new_post)
				db.session.commit()