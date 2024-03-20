from django.contrib import admin
from django.urls import path
from django.urls import include, re_path
from base import views as core_views


urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('base.urls')),
    path('accounts/', include('django.contrib.auth.urls')), #include /login etc
    re_path(r'^signup/$', core_views.signup, name='signup'),
    path('api-auth/', include('rest_framework.urls'))



]
