from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

class IViewProblems(zope.interface.Interface):
    def viewProblems(self):
        pass

