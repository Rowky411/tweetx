
from django.urls import path
from .views import (
    TweetDetailView, 
    TweetListView,
    TweetCreateView,
    TweetUpdateView,
    TweetDeleteView
)

app_name = 'tweets'

urlpatterns = [
    path('', TweetListView.as_view(), name='list'),
    path('create/', TweetCreateView.as_view(), name='create'),  # /tweet/create/
    path('<int:pk>/', TweetDetailView.as_view(), name='detail'),  # /tweet/<pk>/
    path('<int:pk>/update/', TweetUpdateView.as_view(), name='update'),  # /tweet/<pk>/update/
    path('<int:pk>/delete/', TweetDeleteView.as_view(), name='delete'),  # /tweet/<pk>/delete/
]
