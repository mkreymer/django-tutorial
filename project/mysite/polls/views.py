from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

from .models import Choice, Question

# This is the shortcut: render()... which covers (like above)
# template loading, filling context, and returning HttpResponse
def index(request):
	latest_question_list = Question.objects.order_by('-pub_date')[:5]
	context = {'latest_question_list': latest_question_list}
	return render(request, 'polls/index.html', context)
							#this actually takes to just /polls/ checkout urls.py!

def detail(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	return render(request, 'polls/detail.html', {'question': question})
#Raising a 404 error
#-----def detail(request, question_id):
#-----    try:
#-----        question = Question.objects.get(pk=question_id)
#-----    except Question.DoesNotExist:
#-----        raise Http404("Question does not exist")
#-----    return render(request, 'polls/detail.html', {'question': question})
#NOTE: theres a shortcut for this too... the get_object_or_404() function

def results(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	return render(request, 'polls/results.html', {'question': question})

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


	


