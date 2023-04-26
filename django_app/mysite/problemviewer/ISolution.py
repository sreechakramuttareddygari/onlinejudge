import zope.interface
from django.shortcuts import render
from . import IExecute
from . import ILeaderboard
import datetime
from .models import Solutions

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

    def submit(self,request):
        submittedat = datetime.datetime.now()
        self.solutionID = str(submittedat)+str(self.userID)+str(self.problemID)
        outputs = self.runExec()
        print(outputs)
        verdict = self.runEval(outputs)
        solution = Solutions(SolutionID = self.solutionID,Submitted_at=submittedat,ProblemID_id=self.problemID,UserID_id=self.userID,Failed_test_case_id=None,Time_taken=datetime.datetime.now(),Verdict=verdict)
        solution.save()
        print(verdict)
        #Solutions.objects.raw("INSERT INTO problemviewer_Solutions (SolutionID, ProblemID_id, UserID_id, Submitted_at, Failed_test_case_id, succededTestcases,Time_taken,Verdict) VALUES ("+str(self.solutionID)+','+str(self.problemID)+','+str(self.userID)+','+str(submittedat)+','+str(None)+','+str(1)+','+str(0)+','+str(verdict)+")")
        # latest_question_list = Solutions.objects.order_by('SolutionID')[:5]
        leaderboard = ILeaderboard.SimpleLeaderboard()
        return leaderboard.leaderboard(request,self.userID,self.problemID)
    def runExec(self):
        outputs = self.executor.execute(self.code, self.problemID)
        return outputs
    def runEval(self,outputs):
        return self.evaluator.evaluate(outputs)
    def verdict(self):
        pass
