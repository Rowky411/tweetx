from django.contrib import admin

from .models import Tweet
from .forms import TweetModelForm

# Register your models here.

class TweetModelAdmin(admin.ModelAdmin):
    #form  = TweetModelForm
    class Meta:
        model = Tweet   
        

#admin.site.register(Tweet)

admin.site.register(Tweet, TweetModelAdmin)