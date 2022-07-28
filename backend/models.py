from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=60)
    git_url = models.URLField()
    stack = models.CharField(max_length=320)
    images = models.ImageField(upload_to='images/%Y/%m/%d')
    description = models.TextField(blank=True)
    data = models.DateField(auto_now_add=True, db_index=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Проект"
        verbose_name_plural = "Проекты"
