
from django.urls import path
from . import views
urlpatterns = [
    
    path('',views.sign_up),
    path('login/',views.login_user),
    path('user_profile/',views.user_profile,name='user_profile'),
    path('logout/',views.user_logout),
    path('changepass/',views.changepass),
    path('details/',views.details),
    path('uploadPic/<str:user>/',views.uploadPic,name="uploadPic"),
    path('chat/<str:room_name>/', views.room, name='room'),
]
