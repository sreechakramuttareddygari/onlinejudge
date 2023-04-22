from django.urls import path
from . import views
from . import evaluate
from . import website
urlpatterns = [
path('',website.problemlist,name='index'),
path('<int:problemID>/',website.selectproblem,name='detail'),
]
