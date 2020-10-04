from django.urls import path
from . import views


app_name = "cheeses"
urlpatterns = [
    path(
        route="",
        view=views.CheeseListView.as_view(),
        name='list'
    ),
    path(
        route='~add/',
        view=views.CheeseCreateView.as_view(),
        name='add'
    ),    
    path(
        route='<slug:slug>/',
        view=views.CheeseDetailView.as_view(),
        name='detail'
    ),
    path(
        route='<slug:slug>/update/',
        view=views.CheeseUpdateView.as_view(),
        name='update'
    )
]