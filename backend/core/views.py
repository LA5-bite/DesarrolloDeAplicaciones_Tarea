from django.contrib.auth.decorators import login_required
from django.shortcuts import render

def home(request):
    return render(request, "core/home.html")

@login_required
def dashboard(request):
    user = request.user
    if user.is_superuser or user.is_staff:
        role_template = "core/roles/admin.html"
    elif user.role == "GESTOR":
        role_template = "core/roles/manager.html"
    else:
        role_template = "core/roles/user.html"
    return render(request, role_template)
