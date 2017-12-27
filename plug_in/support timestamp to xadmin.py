#coding=utf-8
from xadmin.filters import DateFieldListFilter
from xadmin.filters import manager
import datetime
import time
from django.db import models

TIMESTAMP_FIELD = ['timestamp', '_inter_timestamp']


@manager.register
class TimestampFieldListFilter(DateFieldListFilter):
    @classmethod
    def test(cls, field, request, params, model, admin_view, field_path):
        return isinstance(field, models.IntegerField) & (field_path in TIMESTAMP_FIELD)

    def do_filte(self, queryset):
        params = self.used_params.copy()
        k = params.keys()
        field = self.field_path
        GTE = '%s__gte' % field
        LT = '%s__lt' % field
        YEAR = '%s__year' % field
        MONTH = '%s__month' % field
        DAY = '%s__month' % field

        if (GTE in k) & (LT in k):
            start, end = str(params[GTE]), str(params[LT])
            start_time = int(time.mktime(datetime.datetime.strptime(start, '%Y-%m-%d').timetuple()))
            end_time = int(time.mktime(datetime.datetime.strptime(end, '%Y-%m-%d').timetuple()))
            if '_inter' in field: start_time, end_time = start_time * 1000, end_time * 1000

            params[GTE], params[LT] = start_time, end_time
        elif (YEAR in k) & (MONTH in k) & (DAY in k):
            year, month, day = map(int, map(str, [params[YEAR], params[MONTH],
                                                  params[DAY]]))
            start = datetime.datetime(year=year, month=month, day=day)
            end = start + datetime.timedelta(days=1)
            start_time = int(time.mktime(start.timetuple()))
            end_time = int(time.mktime(end.timetuple()))
            params.clear()
            if '_inter' in field: start_time, end_time = start_time * 1000, end_time * 1000
            params[GTE], params[LT] = start_time, end_time
        else:
            pass
        return queryset.filter(**params)
        
#add in adminx.py
from fix_xadmin_timestamp import TimestampFieldListFilter
from xadmin.filters import manager

manager.register(TimestampFieldListFilter, take_priority=True)
