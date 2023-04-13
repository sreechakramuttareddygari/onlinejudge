from django.urls import path
from . import views
from . import viewseval

urlpatterns = [
path('',views.index,name='index'),
path('eval',viewseval.index,name='index'),
]
