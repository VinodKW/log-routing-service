from django.db import models

# Create your models here.

class Log(models.Model): 
    """

    {
	"id": 1234,
	"unix_ts": 1684129671,
	"user_id": 123456,
	"event_name": "login"}

    """
        
    unix_ts = models.BigIntegerField()
    user_id = models.BigIntegerField()
    event_name = models.CharField(max_length=255)
    

