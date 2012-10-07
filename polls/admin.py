from polls.models import Poll, Choice
from django.contrib import admin

class PollAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'question']
   # fields = ['question', 'pub_date']  ## Cambiar el orden de mostrado de los
   # campos
        
admin.site.register(Poll, PollAdmin)
admin.site.register(Choice)
