from django.urls import path
from syslog_inputs import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = format_suffix_patterns([
    path('', views.api_root),
    path('syslog_inputs/',
         views.SyslogInputList.as_view(),
         name='syslog_input-list'),
    path('syslog_inputs/<int:pk>/',
         views.SyslogInputDetail.as_view(),
         name='syslog_input-detail'),
    path('users/',
         views.UserList.as_view(),
         name='user-list'),
    path('users/<int:pk>/',
         views.UserDetail.as_view(),
         name='user-detail')
])
