"""withrestc6 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from testapp import views
from rest_framework.authtoken import views as views1


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^api/', views.EmployeeListAPIView.as_view()),
    # url(r'^api/', views.EmployeeAPIView.as_view()),
    #url(r'^api/', views.EmployeeCreateAPIView.as_view()),
    # url(r'^api/(?P<id>\d+)/$', views.EmployeeDetailAPIView.as_view()),
    # url(r'^api/(?P<id>\d+)/$', views.EmployeeUpdateAPIView.as_view()),
    # url(r'^api/(?P<id>\d+)/$', views.EmployeeDeleteAPIView.as_view()),
     # url(r'^api/$', views.EmployeeListCreateAPIView.as_view()),
    # url(r'^api/(?P<id>\d+)/$', views.EmployeeRetrieveUpdateAPIView.as_view()),
    # url(r'^api/(?P<id>\d+)/$', views.EmployeeRetrieveDestroyAPIView.as_view()),
    # url(r'^api/(?P<id>\d+)/$', views.EmployeeRetrieveUpdateDestroyAPIView.as_view()),
    url(r'^api/$', views.EmployeeListModelMixin.as_view()),
    url(r'^api/(?P<pk>\d+)/$', views.EmployeeDetailAPIViewMixin.as_view()),
    url(r'^api-token-auth', views1.obtain_auth_token,name='api-token-auth'),
]
