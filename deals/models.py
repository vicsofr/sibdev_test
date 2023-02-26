from django.db import models


class Deal(models.Model):
    customer = models.CharField(max_length=30)
    item = models.CharField(max_length=50)
    total = models.IntegerField()
    quantity = models.IntegerField()
    date = models.DateTimeField()
    last_parse = models.BooleanField(default=True)

    class Meta:
        db_table = 'deals'
        verbose_name = 'Deal'
        verbose_name_plural = 'Deals'
