from . import User
from . import Problem
from . import IViewProblems
from . import ISelectProblem

def problemlist(request):
    listOfProblems = IViewProblems.SimpleView()
    return listOfProblems.viewProblems(request)
def selectproblem(request, problemID):
    selection = ISelectProblem.SimpleSelect()
    return selection.showProblem(request,problemID)
# def








#
# class main():
#     def __int__(self, user):
#         self.user = user
#
#     def pro
#
# def __init__(request):
#     main(request)