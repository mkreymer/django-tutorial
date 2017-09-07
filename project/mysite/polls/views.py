from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


# importing this for the new view which displays latest 5 poll questions 
from .models import Question




def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")




# these views are slightly different because they take an argument:
def detail(request, question_id):
	return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
	response = "You're looking at the results of question %s."
	return HttpResponse(response % question_id)

def vote(request, question_id):
	return HttpResponse("You're voting on question %s." % question_id)
#the above must then be wired into the polls.urls module by adding url() calls



# displays latest 5 poll questions in
# the system, seperated by commas, according to publication date
def index(request):
	latest_question_list = Question.objeccts.order_by('-pub_date')[:5]
	output = ', '.join([q.question_text for q in latest_question_list])
	return HttpResponse(output)
# There's a problem here, though: the page's design is hard-coded in the view. If 
# you want to change the way the page looks, you;ll have to edit this Python code.
# So let's use Django's template system to seperate the design from Python by
# creating a template that the view can use





