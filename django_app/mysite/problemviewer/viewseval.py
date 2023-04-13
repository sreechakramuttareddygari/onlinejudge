from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    problem_list = Problems.objects.order_by('ProblemID')
    context = {'problem_list': problem_list}
    # output = ','.join([q.question_test for q in latest_question_list])
    # return HttpResponse(output)
    return render(request, 'problemviewer/index.html', context)
