from django.conf.urls import url

from . import views


# its important to namespace the url names because if theres more than one
# app in use there will likely be conflict. so for this instance ill add
#app_name = 'polls'

app_name = 'polls'
urlpatterns = [
	# e.g. /polls/
    url(r'^$', views.index, name='index'),
    # ex: /polls/5/
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    #ex: /polls/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),

]
