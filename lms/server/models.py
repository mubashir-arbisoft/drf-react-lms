from django.contrib.auth.models import User
from django.db import models
from django.db.models import Avg, Subquery, Count

class Author(models.Model):
    name = models.CharField(max_length=100, null=False, unique=True)


class Book(models.Model):
    cover = models.ImageField(upload_to='book_cover/%Y/%m/%d', blank=True, null=True)
    title = models.CharField(max_length=100, null=False, unique=True)
    summary = models.CharField(max_length=5000, default='No summary found')
    isbn = models.CharField(max_length=100, null=False, default='1234567')
    language_code = models.CharField(max_length=100, null=False, default='eng')
    author = models.ForeignKey(Author, to_field='name', null=False, on_delete=models.DO_NOTHING, db_column='author')
    published_on = models.DateField(null=True)
    category = models.CharField(max_length=100, default='Unassigned', null=False)
    publisher = models.CharField(max_length=100, default='Unassigned', null=False)
    quantity = models.IntegerField(default=1)
    
    @property
    def avg_rating(self):
        return self.rating_set.aggregate(avg_rating=Avg('rating'))['avg_rating']

    @property
    def total_reviewers(self):
        return self.rating_set.aggregate(count=Count('rating'))['count']

    @property
    def help(self):
        return self.id


    def __str__(self):
        return self.title


class Rating(models.Model):
    rating = models.DecimalField(
        max_digits=2,
        decimal_places=1,
        default=None
    )
    book = models.ForeignKey(Book, to_field='title', null=False, on_delete=models.CASCADE)
    reader = models.ForeignKey(User, to_field='username', null=False, on_delete=models.CASCADE)
    class Meta:
        unique_together = (("book", "reader"),)


class Request(models.Model):
    reader = models.ForeignKey(User, to_field='username', null=False, on_delete=models.DO_NOTHING)
    book = models.ForeignKey(Book, to_field='title', null=False, on_delete=models.DO_NOTHING)
    status = models.CharField(max_length=100, default='pending')
    issue_period_weeks = models.IntegerField(default=1)

    
class Record(models.Model):
    reader = models.ForeignKey(User, to_field='username', null=False, on_delete=models.DO_NOTHING)
    book = models.ForeignKey(Book, to_field='title', null=False, on_delete=models.DO_NOTHING)
    issue_date = models.DateTimeField(auto_now_add=True)
    return_date = models.DateTimeField(null=True)
    fine = models.IntegerField(null=True)
    issue_period_weeks = models.IntegerField(default=1)
    fine_status = models.CharField(max_length=100, default='none')
    