from django.db import models

class Kundalik(models.Model):
    status = [
        ("Boshlanadi", "Boshlanadi"), ("Boshlandi", "Boshlandi"), ("Bajarildi", "Bajarildi")
    ]
    sarlavha = models.CharField(max_length=30, blank=True)
    muddat = models.CharField(max_length=20)
    batafsil = models.CharField(max_length=50)
    status = models.CharField(max_length=50, choices=status)
    def __str__(self):
        return self.sarlavha