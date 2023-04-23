import zope.interface
from django.shortcuts import render
from .models import Solutions

class ILeaderboard(zope.interface.Interface):
    def leaderboard(self):
        pass

@zope.interface.implementer(ILeaderboard)
class SimpleLeaderboard:
    def leaderboard(self,request,userID,ProblemID):
        latest_question_list = Solutions.objects.order_by('SolutionID').filter(ProblemID_id=ProblemID)[:10]
        context = {'solution_list': latest_question_list}
        # output = ','.join([q.question_test for q in latest_question_list])
        # return HttpResponse(output)
        return render(request, 'problemviewer/leaderboard.html', context)