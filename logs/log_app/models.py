from django.db import models


# Create your models here.
class LogData(models.Model):
    date = models.IntegerField(null=True)
    users = models.IntegerField(null=True)
    sessions = models.IntegerField(null=True)
    sessions_per_user = models.FloatField(null=True)

    # def __str__(self):
    #     data = self.date, self.users, self.sessions, self.sessions_per_user
    #     return self.data
