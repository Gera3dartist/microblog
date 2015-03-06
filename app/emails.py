from flask.ext.mail import Message
from app import ADMINS, mail
from flask import render_template
from threading import Thread
from app import app
from app.decorators import asynch

def send_async_email(app, msg):
	with app.app_context():
		mail.send(msg)

@asynch
def send_email(subject, sender, recipients, text_body, html_body):
	msg = Message(subject, sender=sender, recipients=recipients)
	msg.body = text_body
	msg.html = html_body
	with app.app_context():
		mail.send(msg)
	# thr = Thread(target=send_async_email, args=[app, msg])
	# thr.start()


def follower_notification(followed, follower):
	send_email("[microblog] {} is now following you!".format(follower.nickname), 
				ADMINS[0],
				[followed.email],
				render_template("follower_email.txt",
								user=followed, follower=follower),
				render_template("follower_email.html",
					user=followed, follower=follower)
	)
