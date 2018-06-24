# coding= utf-8
from django.contrib.auth.models import User,Group
#from django.contrib.auth.models import UserProfile, Content
from rest_framework import serializers
# Serializers定义了API的表现形式.
class UserSerializer(serializers.ModelSerializer):  # 使用ModelSerializer 来序列化model层
    """序列化user模型"""
    class Meta:
        model = User  # 指定要序列化的模型
        fields = ('username', 'email', 'is_staff')  # 指定要序列化的字段

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')



