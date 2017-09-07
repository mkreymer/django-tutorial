from django.shortcuts import render
from django.http import Http404

# Create your views here.
from django.http import HttpResponse
# the above could be removed with the render short cut... but due to the stub methods 
# for detail, results, and vote remaining. this too shall remain. 

#-----from django.template import loader
#the above import is no longer needed due to the render shortcut
#which loads the template and fills a context and return an HttpResponse object

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

#-----def index(request):
#-----	latest_question_list = Question.objeccts.order_by('-pub_date')[:5]
#-----	output = ', '.join([q.question_text for q in latest_question_list])
#-----	return HttpResponse(output)

# There's a problem here, though: the page's design is hard-coded in the view. If 
# you want to change the way the page looks, you;ll have to edit this Python code.
# So let's use Django's template system to seperate the design from Python by
# creating a template that the view can use

#------------------------------------------------------------------------------

#-----def index(request):
#-----	latest_question_list = Question.objects.order_by('-pub_date')[:5]
#-----	template = loader.get_template('polls/index.html')
#-----	context = {
#-----		'latest_question_list': latest_question_list,
#-----	}
#-----	return HttpResponse(template.render(context, request))
#the above loads the template polls/index.html and passes it a context




# This is the shortcut: render()... which covers (like above)
# template loading, filling context, and returning HttpResponse
def index(request):
	latest_question_list = Question.objects.order_by('-pub_date')[:5]
	context = {'latest_question_list': latest_question_list}
	return render(request, 'polls/index.html', context)


#Raising a 404 error
def detail(request, question_id):
	try:
		question = Question.objects.get(pk=question_id)
	except Question.DoesNotExist:
		raise Http404("Question does not exist")
	return render(request, 'polls/detail.html', {'question': question})

