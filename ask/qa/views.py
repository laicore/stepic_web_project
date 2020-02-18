from django.shortcuts import render
from django.core.paginator import Paginator as Pgn
from django.http import HttpResponse, Http404
from .models import Question, Answer, QuestionManager

# Create your views here.


def getQ(request, id=1):
    try:
        question = Question.objects.get(id=int(id))
    except Question.DoesNotExist:
        raise Http404
    answer = Answer.objects.filter(question_id=int(id))[:]
    return render(request, 'one_q_base.html', {
        'title': question.title,
        'text': question.text,
        'answer': answer
    })


def main_page(request):
    print(request.path_info)
    if request.path_info == '/popular/':
        questions = Question.objects.popular()
    else:
        questions = Question.objects.new()
    limit = 10
    page = int(request.GET.get('page', 1))
    pagintor = Pgn(questions, limit)
    pagintor.baseurl = request.path + '?page='
    page = pagintor.get_page(page)
    return render(request, 'main_page.html',
                  {
                      'page': page
                  })
