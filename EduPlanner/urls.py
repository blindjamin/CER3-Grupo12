# EduPlanner/urls.py
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView,LogoutView
from api.views import home


urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('events/', include('eduplanner.urls')),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),  # Incluir las URLs de la app eduplanner
]
