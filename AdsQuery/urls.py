"""AdsQuery URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
import os
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from Ads import views
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.views.static import serve
from django.conf.urls.static import static


urlpatterns = [
    path('', views.AdListView.as_view()),
    path('admin/', admin.site.urls),
    path('ads/', include('Ads.urls')),
    path('accounts/', include('django.contrib.auth.urls')),  
    url(r'^oauth/', include('social_django.urls', namespace='social')), 
    url(r'^page/(?P<page>\d+)/$', views.AdListView.as_view(), name="page"),

]



BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
urlpatterns += [
    path('favicon.ico', serve, {
        'path': 'favicon.ico',
        'document_root': os.path.join(BASE_DIR, 'home/static'),
    }
    ),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


# Switch to social login if it is configured - Keep for later
try:
    from . import github_settings
    social_login = 'registration/login_social.html'
    urlpatterns.insert(0,
                       path(
                           'accounts/login/', auth_views.LoginView.as_view(template_name=social_login))
                       )
    print('Using', social_login, 'as the login template')
except:
    print('Using registration/login.html as the login template')
