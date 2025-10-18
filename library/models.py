from django.db import models

# Create your models here.
class Books(models.Model):
    Name = models.CharField(max_length=100)
    id = models.IntegerField(primary_key=True)
    def __str__(self):
        return self.Name
class Authors(models.Model):
    name = models.CharField(max_length=100)
    id = models.IntegerField(primary_key=True)
    def __str__(self):
        return self.name
    

class AuthorsBooks(models.Model):
    AuthorID = models.ForeignKey(Authors, on_delete=models.CASCADE, db_column='AuthorID')
    BookId = models.ForeignKey(Books, on_delete=models.CASCADE, db_column='BookId')



