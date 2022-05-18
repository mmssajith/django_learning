from django.urls import path
from . import views


urlpatterns = [
    # path('home', views.home),
    path('home', views.HomeView.as_view()),
    # path('authorize', views.authorized),
    path('authorize', views.AuthorizedView.as_view()),
]
