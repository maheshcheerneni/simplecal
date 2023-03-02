from django.urls import path,include
from myapp import views


urlpatterns = [
    path("cal/",views.calculter,name="cal"),

]