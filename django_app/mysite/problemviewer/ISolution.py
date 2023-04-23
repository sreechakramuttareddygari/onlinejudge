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
        outputs = self.runExec()
        self.runEval(outputs)
    def runExec(self):
        outputs = self.executor.execute(self.code, self.problemID)
        return outputs
    def runEval(self,outputs):
        return self.evaluator.evaluate(outputs)
    def verdict(self):
        pass
