from django.contrib import admin

# Register your models here.

from .models import Question



#-----class Questionadmin(admin.ModelAdmin)
#-----	fields = ['pub_date', 'question_text']
#-----
#-----admin.site.register(Question, QuestionAdmin)
# the above re-orders the way the fields display



#-----class QuestionAdmin(admin.ModelAdmin):
#-----	fieldsets = [
#-----		(None,					{'fields': ['question_text']}),
#-----		('Date Information',	{'fields': ['pub_date']}),
#-----	]
#-----
#-----admin.site.register(Question, QuestionAdmin)
# the above splits up the form into field sets (in other words groups)
# note: the first element of each tuple in 'fieldsets' is the title of the fieldset
# NOTE THIS CODE WAS EDITED OUT BECAUSE ITS BEEN CHANGED WHEN ADDING RELATED OBJECTS - SEE BELOW






#
#	ADDING RELATED OBJECTS: theres two ways to achieve this
#

from .models import Choice # note: or just add it into the top of page like so - import .models Choice, Question

#first way is to register Choice woth the admin just as we id with Question
#-----admin.site.register(Choice)


#this is the second way
#-----class ChoiceInline(admin.StackedInline): (this takes up space by stacking everything)
class ChoiceInline(admin.TabularInline):
	model = Choice
	extra = 1

#Note: then edit the Question registration code - this must now be placed under the ChoiceInline
class QuestionAdmin(admin.ModelAdmin):
	fieldsets = [
		(None,					{'fields': ['question_text']}),
		('Date Information',	{'fields': ['pub_date'], 'classes': ['collapse']}),
	]
	inlines = [ChoiceInline] # adds choices to page that opens up when question is clicked
	list_display = ('question_text', 'pub_date', 'was_published_recently') # adds fields to question list page
	list_filter = ['pub_date'] # this adds a filter sidebar!
	search_fields = ['question_text']


admin.site.register(Question, QuestionAdmin)
#this tells Djano: Choice objects are edited on the Question admin page.

#
#	END-ADDING RELATED OBJECTS-END
#


#
# Customizing the admin change list - the one that displays all the questions in the system
#

# Add the following to the QuesitonAdmin class
# list_display = ('question_text', 'pub_date', 'was_published_recently')





