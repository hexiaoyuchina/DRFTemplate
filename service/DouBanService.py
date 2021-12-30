# -*- coding:utf-8 -*-
from api.models import DouBan


class DoubanService(object):
    def __init__(self, *args, **kwargs):
        self.id = kwargs.get('id')
        self.title = kwargs.get('title', '')
        self.rating_num = kwargs.get('rating_num', '')
        self.votes = kwargs.get('votes', '')
        self.move_type = kwargs.get('move_type', '')
        self.country = kwargs.get('country', '')
        self.time = kwargs.get('time', '')
        self.director = kwargs.get('director', '')
        self.actor = kwargs.get('actor', '')

    def create(self):
        DouBan.objects.create(rating_num=self.rating_num,
                                       title=self.title,
                                       votes=self.votes,
                                       move_type=self.move_type,
                                       country=self.country,
                                       time=self.time,
                                       director=self.director,
                                       actor=self.actor)
        return {"msg": "成功"}

    def update(self):
        douban = DouBan.objects.get(id=self.id)
        if self.title:
            douban.title = self.title
        if self.actor:
            douban.actor = self.actor
        if self.director:
            douban.director = self.director
        if self.time:
            douban.time = self.time
        if self.country:
            douban.country = self.country
        if self.move_type:
            douban.move_type = self.move_type
        if self.votes:
            douban.votes = self.votes
        if self.rating_num:
            douban.rating_num = self.rating_num
        douban.save()
        return {"msg": "更新成功"}

    def delete(self):
        douban = DouBan.objects.get(id=self.id)
        douban.delete()
        return {"msg": "删除成功"}
