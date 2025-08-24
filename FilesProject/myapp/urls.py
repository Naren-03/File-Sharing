from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name= 'myapp' 

urlpatterns = [

    path('home',views.home,name='home'),
    path('register',views.register,name='register'),
    path('signin',views.signin,name='signin'),
    path('upload',views.upload,name='upload'),
    path('success',views.success,name='success'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)