# coding= utf-8
#一个视图类对应了一个序列化的model

from rest_framework import viewsets
from .serializers import UserSerializer, UserProfileSerializer, ContentSerializer
from django.contrib.auth.models import User
from .models import UserProfile, Content


# ViewSets 定义了 视图（view） 的行为.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()  # 把数据取出来 交给 制定的序列化对象去序列化数据
    serializer_class = UserSerializer


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class ContentViewSet(viewsets.ModelViewSet):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer