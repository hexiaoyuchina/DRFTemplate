# -*- coding:utf-8 -*-
import random
from rest_framework.response import Response


class SerializerDataMixin(object):
    def get_serializer_data(self, request):
        data = request.data
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer_data = serializer.validated_data
        return serializer_data

    def drf_json_success_response(self, data={}):
        result = {
            "code": "success",
            "msg": "操作成功",
            'requestId': random.randint(1, 1000),
            'data': data
        }
        return Response(result)
