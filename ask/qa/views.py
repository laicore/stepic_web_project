from django.shortcuts import render,get_object_or_404
from django.core.paginator import Paginator as Pgn
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Question, Answer, QuestionManager
from .forms import *
# Create your views here.


def AskFormView(request):
    if request.method == 'POST':
        ask = AskForm(request.POST)
        if ask.is_valid():
            question = ask.save()
            url = question.get_url()
            return HttpResponseRedirect(url)
    else:
        form = AskForm()

    return render(request, 'add_qa_form.html', {
        'form': form,
    })


def getQ(request, id=1):
    question = get_object_or_404(Question,id=id)
    answers = Answer.objects.filter(question_id=int(id))[:]
    if request.method == 'POST':
        answer = AnswerForm(question, data=request.POST)
        if answer.is_valid():
            ans = answer.save()
            return HttpResponseRedirect(request.path)
    return render(request, 'one_q_base.html', {
        'id': request.path,
        'title': question.title,
        'text': question.text,
        'answer': answers,
        'form': AnswerForm()
    })


def main_page(request):
    if request.path_info == '/popular/':
        questions = Question.objects.popular()
    else:
        questions = Question.objects.new()
    limit = 4
    page = int(request.GET.get('page', 1))
    pagintor = Pgn(questions, limit)
    pagintor.baseurl = request.path + '?page='
    page = pagintor.get_page(page)
    return render(request, 'main_page.html',
                  {
                      'page': page
                  })
