from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.db.models import Q

from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from .models import Tweet
from .mixins import FormUserNeededMixin, UserOwnerMixin
from .forms import TweetModelForm

class TweetCreateView(LoginRequiredMixin, FormUserNeededMixin, CreateView):
    form_class = TweetModelForm
    template_name = 'tweets/create_view.html'
    login_url = "/admin/"

class TweetUpdateView(LoginRequiredMixin, UserOwnerMixin, UpdateView):
    queryset = Tweet.objects.all()
    form_class = TweetModelForm
    template_name = 'tweets/update_view.html'
    success_url = reverse_lazy("tweet:list")  

class TweetDeleteView(LoginRequiredMixin, DeleteView):
    model = Tweet
    template_name = 'tweets/delete_confirm.html' 
    success_url = reverse_lazy("tweet:list")

class TweetDetailView(DetailView):
    queryset = Tweet.objects.all()
    template_name = "tweets/detail_view.html"

    def get_object(self):
        id_ = self.kwargs.get("pk")
        return Tweet.objects.get(id=id_)

class TweetListView(ListView):
    
    def get_queryset(self, *args, **kwargs):
        qs = Tweet.objects.all()
        print(self.request.GET)
        query = self.request.GET.get("q", None)
        if query is not None:
            qs = qs.filter(
                Q(content__icontains=query)|
                Q(user__username__icontains=query)
                )
        return qs  

    def get_context_data(self, *args, **kwargs):
        context = super(TweetListView, self).get_context_data(*args, **kwargs)
        return context


