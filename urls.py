from django.urls import path
from . import views
urlpatterns=[
 path('',views.home),
 path('post/',views.create_post),
 path('like/<int:id>/',views.like),
 path('comment/<int:id>/',views.comment),
 path('login/',views.login_view),
 path('register/',views.register),
 path('logout/',views.logout_view),
]
