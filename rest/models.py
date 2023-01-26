from django.db import models
import uuid
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    id = models.UUIDField(primary_key = True, default = uuid.uuid4(), editable = False)
    first_name = models.CharField(max_length = 50, null = True, blank = True)
    last_name = models.CharField(max_length = 50, null = True, blank = False)
    username = models.CharField(max_length = 100, unique = False)
    event_assoc = models.CharField(max_length = 255, unique = False, blank = True)
    time_stamp = models.DateTimeField(auto_now = True)
    password = models.CharField(max_length = 100)
    history = HistoricalRecords()

    USERNAME_FIELD = 'admin'
    REQUIRED_FIELD = ['username', 'password']

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'

    def save(self, *args, **kwargs):
        self.username = f'{self.first_name}-{self.last_name}'
        super(User, self).save(*args, **kwargs)