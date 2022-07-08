from django.conf.urls import url 
from . import views

app_name = "base_app"

urlpatterns = [
    url(r'^register/$', views.register, name="register"),
    url(r'^login/$', views.user_login, name="login"),
    url(r'^quasi/', views.quasi, name="quasi"),
    url(r'^wall/', views.wall, name="wall")
]