from django.urls import path
from books import views

urlpatterns = [
    path("",views.SelectBookView.as_view(), name="SelectBooks"),
    path("add", views.AddBookView.as_view(), name="AddBook"),
    path("delete/<int:pk>",views.DeleteBookView.as_view(), name="DeleteBook"),
    path("<int:pk>",views.SelectBookView.as_view(), name="SelectBook")
]