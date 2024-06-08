from django.db import models
from django.urls import reverse
from django.core.exceptions import ValidationError
from django.conf import settings

from .validators import validate_content

# Create your models here.


class Tweet(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    content = models.CharField(max_length=200, validators=[validate_content])
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.content)
    
    def get_absolute_url(self):
        return reverse("tweet:detail", kwargs={"pk":self.pk})
    
    # def clean(self, *args, **kwargs):
    #     content = self.content
    #     if content == "abc":
    #         raise ValidationError("Cannot DO")
    #     return super(Tweet, self).clean(*args, **kwargs)