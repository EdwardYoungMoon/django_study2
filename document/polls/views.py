from doctest import OutputChecker
from re import template
from django.http import HttpResponse
from .models import Question, Choice
from django.template import loader
from django.shortcuts import render


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = { 'latest_question_list' : latest_question_list}
    return HttpResponse(template.render(context, request))


def detail(request, question_id):
    return HttpResponse(f"You're looking at question {question_id}.")

def results(request, question_id):
    response = "You're looking at the result of question."
    return HttpResponse(f'{response}{question_id}')

def vote(request, question_id):
    return HttpResponse(f"You're voting on question {question_id}")