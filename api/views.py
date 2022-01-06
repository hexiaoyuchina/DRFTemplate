# -*- coding:utf-8 -*-
from django.shortcuts import render
from rest_framework import viewsets, mixins
from rest_framework.decorators import action
from api.drfmixins import SerializerDataMixin
from service.DouBanService import DoubanService
from api.serializers import CreateSerializer, ListSerializer, RetriveSerializer, UpdateSerializer, DeleteSerializer
from api.models import DouBan
from api.filter import douban_search
# Create your views here.


class HxyViewSets(SerializerDataMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    lookup_field = 'uuid'

    def get_queryset(self):
        return DouBan.objects.all()

    def get_serializer_class(self):  # 默认使用self.serializer_class,如果实现这个方法，调用这个方法
        if self.action == 'create':
            return CreateSerializer
        elif self.action == 'retrieve':
            return RetriveSerializer
        elif self.action == 'list':
            return ListSerializer
        elif self.action == 'update_douban':
            return UpdateSerializer
        elif self.action == 'delete':
            return DeleteSerializer

    def create(self, request, *args, **kwargs):
        serializer_data = self.get_serializer_data(request)
        action = DoubanService(**serializer_data)
        res = action.create()
        return self.drf_json_success_response(res)
    #http://127.0.0.1:8000/api/hxy/{id}--->uuid
    def retrieve(self, request, *args, **kwargs):
        douban = self.get_object()
        serializer = self.get_serializer(douban)
        serializer_data = serializer.data
        return self.drf_json_success_response(serializer_data)
    # @action(metods=['POST'], url_path='my_detail')
    # def my_detail(self, request):
    #     pass

    #http://127.0.0.1:8000/api/hxy/?pageNumber=1&pageSize=20&key="xx'
    def list(self, request, *args, **kwargs):
        data = request.GET
        search = data.get("key", None)

        queryset = self.filter_queryset(self.get_queryset())
        queryset = douban_search(queryset, search)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)

        return self.drf_json_success_response(serializer.data)

    # http://127.0.0.1:8000/api/hxy/update/ data={'''}
    @action(methods=['POST'], detail=False, url_path='update')
    def update_douban(self, request, *args, **kwargs):
        serializer_data = self.get_serializer_data(request)
        action = DoubanService(**serializer_data)
        res = action.update()
        return self.drf_json_success_response(res)

    @action(methods=['POST'], detail=False, url_path='delete')
    def delete(self, request, *args, **kwargs):
        serilizer_data = self.get_serializer_data(request)
        action = DoubanService(**serilizer_data)
        res = action.delete()
        return self.drf_json_success_response(res)

