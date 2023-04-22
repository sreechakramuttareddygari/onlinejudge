import zope.interface
from django.shortcuts import render
from .models import Problems

class IViewProblems(zope.interface.Interface):
    def viewProblems(self):
        pass

@zope.interface.implementer(IViewProblems)
class SimpleView:

    def viewProblems(self,request):
        problem_list = Problems.objects.order_by('ProblemID')
        context = {'problem_list': problem_list}
        # output = ','.join([q.question_test for q in latest_question_list])
        # return HttpResponse(output)
        return render(request, 'problemviewer/index.html', context)