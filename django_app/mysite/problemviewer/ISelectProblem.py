import zope.interface
from django.shortcuts import render
from .models import Testcases
from . models import Problems

class ISelectProblem(zope.interface.Interface):
    def showProblem(self):
        pass

@zope.interface.implementer(ISelectProblem)
class SimpleSelect:
    def showProblem(self,request,problemID):
        problem = Problems.objects.raw('SELECT * FROM problemviewer_Problems WHERE ProblemID='+str(problemID))[0]
        context = {'problem': problem}
        #print(context['problem'])
        # output = ','.join([q.question_test for q in latest_question_list])
        # return HttpResponse(output)
        return render(request, 'problemviewer/showproblem.html', context)