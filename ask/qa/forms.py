from django import forms
from .models import Question, Answer
from django.contrib.auth.models import User


class SignUp(forms.Form):
    username = forms.CharField(max_length=64, min_length=8, label="Логин")
    email = forms.EmailField(max_length=100, min_length=5)
    password = forms.CharField(
        widget=forms.PasswordInput, min_length=8, label="Пароль")

    def save(self):
        user = User.objects.create_user(**self.cleaned_data)
        user.save()
        return user


class LoginIn(forms.Form):
    username = forms.CharField(max_length=64, min_length=8, label="Логин")
    password = forms.CharField(
        widget=forms.PasswordInput, min_length=8, label="Пароль")
    


class AskForm(forms.Form):
    title = forms.CharField(max_length=100,label="Question")
    text = forms.CharField(widget=forms.Textarea,label="text question")
    def __init__(self, user=None, **kwargs):
        self.user = user
        super(AskForm, self).__init__(**kwargs)
    def clean_text(self):
        title = self.cleaned_data['title']
        text = self.cleaned_data['text']
        if text == "" or title == "":
            raise forms.ValidationError(
                'empty lines')
        return text

    def save(self):
        question = Question(**self.cleaned_data, author_id=self.user.id)
        question.save()
        return question


class AnswerForm(forms.Form):
    text = forms.CharField()

    def __init__(self, question=None,user=None, **kwargs):
        self.question = question
        self.user = user
        super(AnswerForm, self).__init__(**kwargs)

    def clean_text(self):
        text = self.cleaned_data['text']
        if text == "":
            raise forms.ValidationError('empty line')
        return text

    def save(self):

        answer = Answer(**self.cleaned_data, author_id=self.user.id,
                        question_id=self.question.id)
        answer.save()
        return answer
