import zope.interface
from django.shortcuts import render
from .models import Testcases
from . models import Problems
from django.http import JsonResponse

class ISelectProblem(zope.interface.Interface):
    def showProblem(self):
        pass

@zope.interface.implementer(ISelectProblem)
class SimpleSelect:
    def showProblem(self,request,problemID):
        problem = Problems.objects.raw('SELECT * FROM problemviewer_Problems WHERE ProblemID='+str(problemID))[0]
        context = {'ProblemID': problem.ProblemID,'ProblemName':problem.ProblemName,'Statement':problem.Statement,'Difficuly':problem.Difficuly}
        #print(context['problem'])
        # output = ','.join([q.question_test for q in latest_question_list])
        # return HttpResponse(output)
        print(problem)
        return JsonResponse(context)
        #return render(request, 'problemviewer/showproblem.html', context)