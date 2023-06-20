from . import User
from . import Problem
from . import IViewProblems
from . import ISelectProblem
from . import IExecute
from . import ISolution
from . import IEvaluator
from .models import Problems

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import *


@api_view(['OPTIONS','GET', 'POST'])
def problem_list(request):
    print('hello')
    if request.method == 'GET':
        print('he')
        data = Problems.objects.all()

        serializer = ProblemSerializer(data, context={'request': request}, many=True)

        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ProblemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def problemlist(request):
    listOfProblems = IViewProblems.SimpleView()
    return listOfProblems.viewProblems(request)
def selectproblem(request, problemID):
    selection = ISelectProblem.SimpleSelect()
    return selection.showProblem(request,problemID)
def submitSolution(request, problemID):
    code = request.POST['code']
    executor = IExecute.SimpleExecutorCPP()
    evaluator = IEvaluator.BitwiseEvaluator()
    solution = ISolution.PracticeSolution(code=code,problemID=problemID,executor=executor,evaluator=evaluator)
    return solution.submit(request)
    #code,language,problemID,executor,evaluator,solutionID,userID








#
# class main():
#     def __int__(self, user):
#         self.user = user
#
#     def pro
#
# def __init__(request):
#     main(request)