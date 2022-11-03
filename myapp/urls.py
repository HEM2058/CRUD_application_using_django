from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.InserPageView,name="insertpage"),
    path("insert/",views.InsertData,name="insert"),
    path("showpage/",views.ShowPage,name="showpage"),
    path("editpage/<int:pk>",views.EditPage,name="editpage"),
    path("updatedata/<int:pk>",views.UpdateData,name="update"),
    path("delete/<int:pk>",views.DeleteData,name="delete")
]