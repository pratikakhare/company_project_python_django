from django.urls import path,include
from django.contrib import admin
from . import views
# from trainer import views as trainer_views

#Originally created by me

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('trainer.urls')),
    path('', include('trainer.urls')),
    
]