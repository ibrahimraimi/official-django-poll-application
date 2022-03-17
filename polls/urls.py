from django.urls import path
from . import views

app_name = "polls"

urlpatterns = [
    # ex: http://127.0.0.1:8000/polls
    path("",  views.IndexView.as_view(), name="index"),

    # ex: http://127.0.0.1:8000/polls/1
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),

    # ex: http://127.0.0.1:8000/polls/1/results
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),

    # ex: http://127.0.0.1:8000/polls/1/vote
    path("<int:question_id>/vote/", views.vote, name="vote")
]
