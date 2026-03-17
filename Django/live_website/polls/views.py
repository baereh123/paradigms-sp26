from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from polls.models import Question


# Create your views here.
def hello(request):
	return render(request, "polls/index.html")

def home(request):
    latest_questions = Question.objects.order_by('-pub_date')#[:5]

    context = {
        "questions": latest_questions,
    }
    return render(request,
                  "polls/question_list.html",
                  context)

class HomeView(ListView):
    model = Question
    paginate_by = 20
    context_object_name = "questions"


class QuestionView(DetailView):
    model = Question
    # template_name = question_detail.html (default)

def vote(request):
    pass