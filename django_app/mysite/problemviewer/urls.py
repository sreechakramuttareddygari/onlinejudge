from django.urls import path
from . import views
from . import IEvaluator
from . import website
urlpatterns = [
path('',website.problemlist,name='index'),
path('<int:problemID>/',website.selectproblem,name='detail'),
path('<int:problemID>/submit/', website.submitSolution, name='submit'),
]
