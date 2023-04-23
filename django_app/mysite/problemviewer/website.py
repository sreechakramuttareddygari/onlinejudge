from . import User
from . import Problem
from . import IViewProblems
from . import ISelectProblem
from . import IExecute
from . import ISolution
from . import IEvaluator

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
    solution.submit()
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