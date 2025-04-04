from django.urls import path,include
from django.contrib import admin
from . import views
#Originally created by me

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('trainer/', include('trainer.urls')),
    
]