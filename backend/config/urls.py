from django.contrib import admin
from django.urls import path
from accounts import views as account_views
from core import views as core_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", core_views.home, name="home"),
    path("registro/", account_views.register, name="register"),
    path("iniciar-sesion/", account_views.login_view, name="login"),
    path("cerrar-sesion/", account_views.logout_view, name="logout"),
    path("panel/", core_views.dashboard, name="dashboard"),
]
