from django.shortcuts import render
from django.http import HttpResponse
import zope.interface
# Create your views here.

class IViewProblems(zope.interface.Interface):
    def viewProblems(self):
        pass

