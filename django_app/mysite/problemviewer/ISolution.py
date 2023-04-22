import zope.interface
from django.shortcuts import render
from . import IExecute

class ISolution(zope.interface.Interface):
    def submit(self):
        pass
    def runExec(self):
        pass
    def runEval(self):
        pass
    def verdict(self):
        pass

@zope.interface.implementer(ISolution)
class PracticeSolution:
    def __init__(self,code,language=None,problemID=None,executor=None,evaluator=None,solutionID=None,userID=None):
        self.code = code
        self.language = language
        self.problemID = problemID
        self.executor = executor
        self.evaluator = evaluator
        self.solutionID = solutionID
        self.userID = userID

    def submit(self):
        self.executor.execute(self.code)

    def runExec(self):
        pass
    def runEval(self):
        pass
    def verdict(self):
        pass
