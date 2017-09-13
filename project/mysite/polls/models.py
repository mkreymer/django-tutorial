import datetime 

from django.db import models
from django.utils import timezone

# Create your models here.

class Question(models.Model):
	question_text = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')

	def was_published_recently(self):
		#-----return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
		#-----Amending the above as the test was failed for this
		now = timezone.now()
		return now - datetime.timedelta(days=1) <= self.pub_date <= now

	def __str__(self):
		return self.question_text



class Choice(models.Model):
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)

	def __str__(self):
		return self.choice_text 





#---------------------------------------------------------------------------
# so how is choice_set called into existance???????????
# heres the answer!!!!!!!!!!!!!!

# You created a foreign key on Choice which relates each one to a Question.

# So, each Choice explicitly has a question field, which you declared in the model.

# Django's ORM follows the relationship backwards from Question too, automatically 
# generating a field on each instance called foo_set where Foo is the model with a 
# ForeignKey field to that model. 

# choice_set is a RelatedManager which can create
# querysets of Choice objects which relate to the Question instance, e.g. q.choice_set.all()

# If you don't like the foo_set naming which Django chooses automatically, or if you have 
# more than one foreign key to the same model and need to distinguish them, you can choose
# your own overriding name using the related_name argument to ForeignKey

#source: https://stackoverflow.com/questions/2048777/django-tutorial-what-is-choice-set
#--------------------------------------------------------------------------------