from django.urls import path, include
from news import views
from .router import router

urlpatterns = [
    path('', views.home, name='home'),
    path('api/', include(router.urls))
]
