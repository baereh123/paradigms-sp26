from django.urls import path
from django.views.generic import DetailView

from polls.views import home, HomeView, QuestionView, vote
app_name = 'polls'
urlpatterns = [
    # path("", home, name="home"),
    path("", HomeView.as_view(), name="home"),
    path('<int:pk>/', QuestionView.as_view(), name="detail"),
    path("somethingForNow/<int:pk>", vote, name="vote"),
]