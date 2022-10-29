from django.db import models

# Create your models here.
ACCOUNT_STATUS_CHOICE = (
        ('Deactivated','Deactivated'),
        ('Activated', 'Activated'),
        )

class Member(models.Model):
    COFFEE_VARIETY_CHOICE = [
        ('SL28','SL28'),
        ('SL34','SL34'),
        ('Ruiru 11','Ruiru 11'),
        ('Batian','Batian'),
    ]
    mem_number=models.PositiveIntegerField(default=0, blank=False, unique=True, editable=False)
    first_name=models.CharField(max_length=256)
    last_name=models.CharField(max_length=256)
    id_no=models.PositiveIntegerField(default=0, blank=False, unique=True, editable=False)
    address=models.CharField(max_length=256)
    farm_size=models.CharField(max_length=256)
    variety=models.CharField(choices=COFFEE_VARIETY_CHOICE, default='Batian', max_length=200)
    contact=models.PositiveIntegerField(default=0, blank=False, unique=True, editable=False)
    status=models.CharField(choices=ACCOUNT_STATUS_CHOICE, default='Activated', max_length=11,editable=False)
    date_created=models.DateTimeField(auto_now_add=True)
    date_updated=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.mem_number + " " + self.last_name + " " + self.first_name