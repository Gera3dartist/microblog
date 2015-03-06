# -*- coding: utf-8 -*-
import os
import unittest
from config import basedir
from app import app, db
from app.models import User, Post
from datetime import datetime, timedelta
from app.translate import microsoft_translate
from coverage import coverage
cov = coverage(branch=True, omit=['flask/*', 'tests.py'])
cov.start()


class TestCase(unittest.TestCase):
	def setUp(self):
		app.config['TESTING'] = True
		app.config['WTF_CSRF_ENABLED'] = False
		app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, \
			'test.db')
		self.app = app.test_client()
		db.create_all()

	def tearDown(self):
		db.session.remove()
		db.drop_all()

	def test_avatar(self):
		"testing avatar"
		u = User(nickname='john', email='john@example.com')
		avatar = u.avatar(128)
		expected = 'http://www.gravatar.com/avatar/d4c74594d841139328695756648b6bd6'
		assert avatar[0:len(expected)] == expected

	def test_make_unique_nickname(self):
		"testing handling of dupliacated names"
		u = User(nickname='john', email='john@examlple.com')
		db.session.add(u)
		db.session.commit()
		nickname = User.make_unique_nickname('john')
		self.assertNotEquals(nickname,'john')
		u = User(nickname=nickname, email='susan@example.com')
		db.session.add(u)
		db.session.commit()
		nickname2 = User.make_unique_nickname('john')
		self.assertNotEquals(nickname2,'john')
		self.assertNotEquals(nickname2,nickname)

	@unittest.expectedFailure
	def test_fail(self):
		"this test should fail"
		self.assertEqual(1, 0, 'broken')

	def test_assert_raises_reges(self):
		"testing exception contains pattern"
		with self.assertRaisesRegexp(ValueError, 'literal'):
	   		int('XYZ')
    
	def test_follow(self):
		"testing follow functionality"
		u1 = User(nickname='john', email='john@whatever.com')
		u2 = User(nickname='susan', email='susan@whatever.com')
		db.session.add(u1)
		db.session.add(u2)
		db.session.commit()
		assert u1.unfollow(u2) is None
		u = u1.follow(u2)
		db.session.add(u)
		db.session.commit()
		assert u1.follow(u2) is None
		assert u1.is_following(u2)
		assert u1.followed.count() == 1
		assert u1.followed.first().nickname == 'susan'
		assert u2.followers.count() == 1
		assert u2.followers.first().nickname == 'john'
		u = u1.unfollow(u2)
		assert u is not None
		db.session.add(u)
		db.session.commit()
		assert not u1.is_following(u2)
		assert u1.followed.count() == 0
		assert u2.followers.count() == 0

	def test_follow_posts(self):
		"testing following of users posts"
		# make four users
		posts = []
		names = ('john','susan','mary','david')
		users = [User(nickname=n, \
				email='{}@domain.com'.format(n)) for n in names]
		for u in users:
			db.session.add(u)
		# make four posts
		utcnow = datetime.utcnow()
		for n in xrange(len(names)):
			post = Post(body="post from {}".format(names[n]), \
					 author=users[n], timestamp=utcnow + timedelta(seconds=n+1))
			posts.append(post)
			db.session.add(post)
		db.session.commit()
		# setup the followers
		users[0].follow(users[0])
		users[0].follow(users[1])
		users[0].follow(users[3])
		users[1].follow(users[1])
		users[1].follow(users[2])
		users[2].follow(users[2])
		users[2].follow(users[3])
		users[3].follow(users[3])
		for u in users:
			db.session.add(u)
		db.session.commit()
		# check the followed posts of each user
		f1 = users[0].followed_posts().all()
		f2 = users[1].followed_posts().all()
		f3 = users[2].followed_posts().all()
		f4 = users[3].followed_posts().all()
		assert len(f1) == 3
		assert len(f2) == 2
		assert len(f3) == 2
		assert len(f4) == 1
		assert f1 == [posts[3], posts[1], posts[0],]
		assert f2 == [posts[2], posts[1]]
		assert f3 == [posts[3],posts[2]]
		assert f4 == [posts[3]]


	def test_forward_translation(self):
		"testing forward translation"
		assert microsoft_translate(u'English', 'en', 'uk') == u'Англійська'

	def test_backward_translation(self):
		"testing backward translation "
		assert microsoft_translate(u'Англійська','uk','en') == u'English'






if __name__ == '__main__':
	try:
		suite = unittest.TestLoader().loadTestsFromTestCase(TestCase)
		# fast_suite = unittest.TestSuite(map(TestCase, ['test_forward_translation', 'test_backward_translation']))
		unittest.TextTestRunner(verbosity=2).run(suite)
	except:
		pass
	cov.stop()
	cov.save()
	print "\n\nCoverage report:\n"
	cov.report()
	print "HTML version: " + os.path.join(basedir, "tmp/coverage/index.html")
	cov.html_report(directory='tmp/coverage')
	cov.erase()




















