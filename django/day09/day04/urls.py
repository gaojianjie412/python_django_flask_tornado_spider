"""day04 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, include, re_path
from django.contrib.staticfiles.urls import static

from app import views

from day04.settings import MEDIA_URL, MEDIA_ROOT, DEBUG

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('index/', views.index),
    path('app/', include(('app.urls', 'app'), namespace='app')),
    path('user/', include(('user.urls', 'user'), namespace='user')),
    # path('goods/', include('goods.urls')),
    # path('app/', include(('app.urls', 'app')))
]


from django.contrib.staticfiles.urls import static
urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)

if DEBUG:
    import debug_toolbar
    urlpatterns.append(re_path(r'^__debug__/', include(debug_toolbar.urls)))
