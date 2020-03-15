from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator as Pgn
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import *
from .forms import *
from django.contrib.auth import authenticate, login, logout,models


def signUp(request):
    if request.method == "POST":
        _signup = SignUp(request.POST)
        if _signup.is_valid():
            user = _signup.save()
            user = authenticate(username=user.username,
                                password=request.POST['password'])
            login(request, user)
            return HttpResponseRedirect('/')
    form = SignUp()
    return render(request, 'signup.html',
                  {
                      'actionPath': request.path,
                      'form': form,
                  })


def logOut(request):
    logout(request)
    return HttpResponseRedirect('/')


def loginIn(request):
    user = request.user
    if user.is_authenticated:
        return HttpResponseRedirect('/')

    if request.method == 'POST':
        if not user.is_authenticated:
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            _user = LoginIn(request.POST)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                return HttpResponse('wrong login or password')
    form = LoginIn()
    return render(request, 'signup.html', {
        'actionPath': request.path,
        'form': form
    })


def AskFormView(request):
    if request.method == 'POST':
        user = models.User.objects.get(username= request.user)
        ask = AskForm(user=user, data=request.POST)
        if ask.is_valid():
            question = ask.save()
            url = question.get_url()
            return HttpResponseRedirect(url)
    else:
        if request.user.is_authenticated:
            form = AskForm()
        else:
            return HttpResponseRedirect('/login')

    return render(request, 'add_qa_form.html', {
        'form': form,
    })


def getQ(request, id=1):
    question = get_object_or_404(Question, id=id)
    answers = Answer.objects.filter(question_id=int(id))[:]
    if request.method == 'POST' and request.user.is_authenticated:
        user = models.User.objects.get(username= request.user)
        answer = AnswerForm(question,user, data=request.POST)
        if answer.is_valid():
            ans = answer.save()
            return HttpResponseRedirect(request.path)
    return render(request, 'one_q_base.html', {
        'login': request.user,
        'questionUser': question.author,
        'id': request.path,
        'title': question.title,
        'text': question.text,
        'answer': answers,
        'form': AnswerForm() if request.user.is_authenticated else None,
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
