# -*- coding:utf-8 -*-
from django.db import models

# Create your models here.


class DouBan(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255, default='', help_text="标题")
    rating_num = models.CharField(max_length=255, default='', help_text='评分')
    votes = models.CharField(max_length=255, default='', help_text='投票人数')
    move_type = models.CharField(max_length=255, default='', help_text='电影类型')
    country = models.CharField(max_length=255, default='', help_text='国家')
    time = models.CharField(max_length=255, default='', help_text='时长')
    director = models.CharField(max_length=255, default='', help_text='导演')
    actor = models.CharField(max_length=255, default='', help_text='演员')

    class Meta:
        db_table = 'douban'
        managed = False

    @property
    def country_cn(self):
        if self.country == 'china':
            return "中国"
        elif self.country == 'america':
            return "美国"
