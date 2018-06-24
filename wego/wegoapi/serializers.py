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






from rest_framework import serializers
from wegoapi.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES
class SnippetSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=False, allow_blank=True, max_length=100)
    code = serializers.CharField(style={'base_template': 'textarea.html'})
    linenos = serializers.BooleanField(required=False)
    language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
    style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Snippet.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.code = validated_data.get('code', instance.code)
        instance.linenos = validated_data.get('linenos', instance.linenos)
        instance.language = validated_data.get('language', instance.language)
        instance.style = validated_data.get('style', instance.style)
        instance.save()
        return instance
#
# class UserProfileSerializer(serializers.ModelSerializer):
#     """序列化userprofile 模型"""
#
#     class Meta:
#         model = UserProfile
#         fields = ('age', 'image')
#
#
# class ContentSerializer(serializers.ModelSerializer):
#     """content 模型"""
#
#     class Meta:
#         model = Content
#         fields = ('name', 'age', 'image')