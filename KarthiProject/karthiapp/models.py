from django.db import models
from datetime import date
from django.utils.timezone import now
kumonpg = [
    ('1', '1 page'),
    ('3', '2 pages'),
    ('4', '4 pages'),
    ('5', '5 pages'),
    ('6', '6 pages'),
('7', '7 pages'),
('8', '8 pages'),
('9', '9 pages'),
('1b', '1 book'),
]

class KarthiData(models.Model):
    name=models.CharField(max_length=56)
    playtime=models.IntegerField()
    cycletime=models.IntegerField()
    kumonpages=models.CharField(choices=kumonpg,max_length=10)
    schoolhomework=models.CharField(max_length=56)
    comments=models.TextField(max_length=256)
    date = models.DateField(default=date.today)



