from django.urls import path
from . import views
from . import IEvaluator
from . import website

urlpatterns = [
path('',website.problem_list,name='index'),
#path('<int:problemID>/',website.problem_list,name='detail'),
path('<int:problemID>/',website.selectproblem,name='detail'),
path('<int:problemID>/submit/', website.submitSolution, name='submit'),
]
