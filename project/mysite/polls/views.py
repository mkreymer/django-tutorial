from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Choice, Question

from django.utils import timezone

# This is the shortcut: render()... which covers (like above)
# template loading, filling context, and returning HttpResponse\
# 
#-----def index(request):
#-----	latest_question_list = Question.objects.order_by('-pub_date')[:5]
#-----	context = {'latest_question_list': latest_question_list}
#-----	return render(request, 'polls/index.html', context)
							    #^^^ this actually takes to just /polls/ ... checkout urls.py!

#-----def detail(request, question_id):
#-----	question = get_object_or_404(Question, pk=question_id)
#-----	return render(request, 'polls/detail.html', {'question': question})

#-----def results(request, question_id):
#-----	question = get_object_or_404(Question, pk=question_id)
#-----	return render(request, 'polls/results.html', {'question': question})

# for the above 3 segments ^^^^^^
# 'question' and 'latest_question_list' are context variables.
# these context variables are then provided to the templates
# NOTE NAME: AAA



class IndexView(generic.ListView):
	template_name = 'polls/index.html'
	context_object_name = 'latest_question_list'

	def get_queryset(self):
		"""
		return the last five published questions (not including those set 
		to be published in the future 
		"""
		return Question.objects.filter(  #returns a queryset containg 'Question's whose pub. date 
			pub_date__lte=timezone.now()  #^ is less than or equal to - that is, earlier than or equal to - timezone.now
		).order_by('-pub_date')[:5]
		#-----return Question.objects.order_by('-pub_date')[:5]
		#the above is before filtering out those set to be pub. in future

class DetailView(generic.DetailView):
	model = Question
	template_name = 'polls/detail.html'
	def get_queryset(self):
		"""
		Excludes any questions that aren't published yet.
		"""
		return Question.objects.filter(pub_date__lte=timezone.now())
		

class ResultsView(generic.DetailView):
	model = Question
	template_name = 'polls/results.html'

# In previous parts of the tutorial, the templates have been provided with a context that 
# contains the question and the latest_question_list context variable. For DetaiLView the 
# question variable is provideed automatically - since we're using a Django model (Question), Django
# is able to determine an appropriate name for the context variable. However, for ListView,
# the automatically generated context variable is question_list. To override this we provide the
# context_object_name attribute, specifying the we want to use latest_quesiton_list instead. As an 
# alternative approach, you could change your templates to match the new default context variables - 
# but it's a lot easier to just tell Django to use the variable you want.




# WARNING!!!!!!!
# This does not avoid race conditions!
def vote(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	try:
		selected_choice = question.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		# Redisplay the question voting form.
		return render(request, 'polls/detail.html', {
			'question': question,
			'error_message': "You didn't select a choice.",
			})
	else:
		selected_choice.votes += 1
		selected_choice.save()
		#Always return an HttpResponseRedirect after successfully dealing with
		#POST data. This preevnts data from being posted twiec if a user hits the back button
		return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
		# We are using the reverse() function in the HttpResponseRedirect constructor in this example. 
		# This function helps avoid having to hardcode a URL in the view function. It is given the 
		# name of the view that we want to pass control to and the variable portion of the URL pattern
		# that points to that view. In this case, using the URLconf we set up in Tutorial 3, 
		# this reverse() call will return a string like '/polls/3/results/' where the 3 is the value of question.id.
		# This redirected URL will then call the 'results' view to display the final page.


	








#Raising a 404 error ... NOTE: this is 2 versions older :ENDNOTE
#-----def detail(request, question_id):
#-----    try:
#-----        question = Question.objects.get(pk=question_id)
#-----    except Question.DoesNotExist:
#-----        raise Http404("Question does not exist")
#-----    return render(request, 'polls/detail.html', {'question': question})
#NOTE: theres a shortcut for this too... the get_object_or_404() function
