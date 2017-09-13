from django.test import TestCase

# Create your tests here.
import datetime

from django.utils import timezone
from django.test import TestCase

from .models import Question


class QuestionModelTests(TestCase):

	def test_was_published_recently_with_future_question(self):
		"""
		was_published_recently() returns False for questions whose pub_date is in the future.
		"""
		time = timezone.now() + datetime.timedelta(days=30)
		future_question = Question(pub_date=time)
		self.assertIs(future_question.was_published_recently(), False)

		"""
		What we have done here is created a 'django.test.TestCase' subclass with a method
		that creates a 'Question' instance with a 'pub_date' in the future. We then check the 
		output of 'was_published_recently()' - which ought to be False.
		"""	
	def test_was_published_recently_with_old_question(self):
		"""
		was_published_recently() returns False for questions whose pub_date is older than 1 day.
		"""
		time = timezone.now() - datetime.timedelta(days=1, seconds=1) 
		old_question = Question(pub_date=time)
		self.assertIs(old_question.was_published_recently(), False)

	def test_was_published_recently_with_recent_questions(self):
		"""
		was_published_recently() returns True for questions whose pub_date is within the last day.
		"""
		time= timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
		recent_question = Question(pub_date=time)
		self.assertIs(recent_question.was_published_recently(), True)

