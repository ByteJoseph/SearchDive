from django.urls import path
try:
   from . import views
except:
   import views

urlpatterns = [
    path("",views.search,name="search"),
    
]