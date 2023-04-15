from django.urls import path
from . import views
from . import evaluate

urlpatterns = [
path('',views.index,name='index'),
path('eval',viewseval.index,name='index'),
]
