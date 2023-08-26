from django.shortcuts import render
from rest_framework.response import Response
from syslog_inputs.models import SyslogInput
from syslog_inputs.serializers import SyslogInputSerializer
from rest_framework import status
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import mixins
from rest_framework import generics
from django.contrib.auth.models import User
from syslog_inputs.serializers import UserSerializer
from rest_framework import permissions
from syslog_inputs.permissions import IsOwnerOrReadOnly
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'sysloginputs': reverse('syslog_input-list', request=request, format=format)
    })

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class SyslogInputList(generics.ListCreateAPIView):
    queryset = SyslogInput.objects.all()
    serializer_class = SyslogInputSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class SyslogInputDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = SyslogInput.objects.all()
    serializer_class = SyslogInputSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
