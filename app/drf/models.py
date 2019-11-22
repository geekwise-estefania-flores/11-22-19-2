from django.db import models

class Bank(models.Model):
    bank_name = models.CharField(max_length = 100)
    bank_phone_number = models.CharField(max_length = 12)

    def __str__(self):
        return(f'BANK NAME: {self.bank_name} | BANK PHONE NUMBER: {self.bank_phone_number}')

