# -*- coding:utf-8 -*-
from rest_framework import serializers
from api.models import DouBan


class CreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = DouBan
        fields = ('title', 'rating_num', 'votes', 'move_type', 'country', 'time', 'director', 'actor')


class RetriveSerializer(serializers.ModelSerializer):
    class Meta:
        model = DouBan
        fields = ('title', 'rating_num', 'votes', 'move_type', 'country', 'time', 'director', 'actor')


class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = DouBan
        fields = ('title', 'rating_num', 'votes', 'move_type', 'country', 'country_cn', 'time', 'director', 'actor')


class UpdateSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=True)
    title = serializers.CharField(required=False,)
    rating_num = serializers.CharField(required=False)
    votes = serializers.CharField(required=False)
    move_type = serializers.CharField(required=False)
    country = serializers.CharField(required=False)
    time = serializers.CharField(required=False)
    director = serializers.CharField(required=False)
    actor = serializers.CharField(required=False)


class DeleteSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=True)
