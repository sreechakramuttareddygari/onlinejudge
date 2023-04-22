import zope.interface
from django.shortcuts import render

class IExecutor(zope.interface.Interface):
    def execute(self):
        pass

class SimpleExecutor(IExecutor):
    def execute(self):
