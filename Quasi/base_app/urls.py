from django.conf.urls import url 
from . import views

app_name = "base_app"

urlpatterns = [
    url(r'^register/$', views.register, name="register"),
    url(r'^login/$', views.user_login, name="login"),
    url(r'^feedback/', views.feedback_form, name="feedback"),
    url(r'^wall/', views.wall, name="wall"),
    url(r'^trauma/', views.trauma, name="trauma"),
    url(r'^youto/', views.youto, name="youto")
]