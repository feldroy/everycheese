from django.urls import path
from . import views


app_name = "cheeses"
urlpatterns = [
    path(
        route="",
        view=views.CheeseListView.as_view(),
        name='list'
    )

]