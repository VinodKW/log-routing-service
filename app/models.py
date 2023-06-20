from django.db import models


class Log(models.Model):
    unix_ts = models.BigIntegerField()
    user_id = models.BigIntegerField()
    event_name = models.CharField(max_length=255)
    