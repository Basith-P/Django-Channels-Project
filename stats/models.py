from django.db import models
from django.utils.text import slugify


class Statistic(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(blank=True)

    @property
    def data(self):
        return self.dataitem_set.all()

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class DataItem(models.Model):
    statistic = models.ForeignKey(Statistic, on_delete=models.CASCADE)
    value = models.PositiveSmallIntegerField()
    owner = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f"{self.owner}: {self.value}"
