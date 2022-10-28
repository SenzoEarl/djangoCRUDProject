from django.db import models


# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=40)
    surname = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return "%s %s" % (self.name, self.surname)


class Category(models.Model):
    title = models.CharField(max_length=40)

    def __str__(self):
        return self.title


class Book(models.Model):
    title = models.CharField(max_length=100)
    quantity_received = models.IntegerField()
    created = models.DateField(auto_now_add=True)
    fiction = models.BooleanField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['created']

