from django.urls import path
from . import views
from . import evaluate
from . import website
urlpatterns = [
path('',website.problemlist,name='index'),
# path('eval',viewseval.index,name='index'),
]
