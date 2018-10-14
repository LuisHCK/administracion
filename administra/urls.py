"""administra URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'', include('apps.dashboard.urls')),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'login'}, name='logout'),
    #url(r'^grappelli/', include('grappelli.urls')), # grappelli URLS
    url(r'^admin/', admin.site.urls),
    url(r'^inventory/', include('apps.inventory.urls')),
    url(r'^sales/', include('apps.sales.urls')),
    url(r'^cash/', include('apps.cash.urls')),
    url(r'^services/', include('apps.services.urls')),
    url(r'^invoices/', include('apps.invoices.urls')),
    url(r'^profiles/', include('apps.profiles.urls')),
    url(r'^settings/', include('apps.settings.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
