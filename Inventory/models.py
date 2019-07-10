from django.db import models

class Status(models.Model):
    created=models.CharField(max_length=20)
    customer_name=models.CharField(max_length=50)
    reference_order=models.CharField(max_length=50)
    products = models.CharField(max_length=50)

    def __str__(self):
        return self.customer_name


class Email(models.Model):
    email_id=models.CharField(max_length=50)

    def __str__(self):
        return self.email_id
