"""shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from store.views import index, product_detail, add_to_card
from shop import settings
from django.conf.urls.static import static
from accounts.views import signup, logout_user, login_user

urlpatterns = [
    path('', index, name='index'),
    path('admin/', admin.site.urls),
    path('product/<str:slug>', product_detail, name="product"),
    path('product/<str:slug>/add_to_card', add_to_card, name="add_to_card"),
    path('signup', signup, name="signup"),
    path('logout', logout_user, name="logout"),
    path('login', login_user, name="login"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
