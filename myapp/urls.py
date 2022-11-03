from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.InserPageView,name="insertpage"),
    path("insert/",views.InsertData,name="insert"),
    path("showpage/",views.ShowPage,name="showpage")
]