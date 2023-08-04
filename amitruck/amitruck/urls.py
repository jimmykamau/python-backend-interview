"""
URL configuration for amitruck project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
import api.views as api_views
from django.contrib import admin
from django.urls import include, path
from rest_framework.authtoken import views as rest_framework_auth_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-token-auth/", rest_framework_auth_views.obtain_auth_token),
    path("", api_views.GetCreateTripApiView.as_view(), name="get-create-trip"),
]
