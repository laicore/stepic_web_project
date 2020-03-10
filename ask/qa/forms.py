#!/usr/bin/python
# -*- coding: utf-8 -*-
from django import forms
from .models import Question, Answer


class AskForm(forms.Form):
    title = forms.CharField(max_length=100)
    text = forms.CharField(widget=forms.Textarea)

    def clean_text(self):
        title = self.cleaned_data['title']
        text = self.cleaned_data['text']
        if text == "" or title == "":
            raise forms.ValidationError(
                'Поле вопроса или названия пустое!', code='empty')
        return text

    def save(self):
        question = Question(**self.cleaned_data, author_id=1)
        question.save()
        return question


class AnswerForm(forms.Form):
    text = forms.CharField()

    def __init__(self, question, **kwargs):
        self.question = question
        super(AnswerForm, self).__init__(**kwargs)

    def clean_text(self):
        text = self.cleaned_data['text']
        if text == "":
            raise forms.ValidationError('Поле ответа пустое!', code='empty')
        return text

    def save(self):

        answer = Answer(**self.cleaned_data, author_id=1,
                        question_id=self.question.id)
        answer.save()
        return answer
