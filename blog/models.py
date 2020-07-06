from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Category(models.Model):
    """
    Django requires models to inherit models.Model class.
    Category only needs a simple category name name.
    CharField specifies the data type of the category name name, CharField is a character type,
    The max_length parameter of CharField specifies its maximum length, and category names that exceed this length cannot be stored in the database.
    Of course, Django also provides us with many other data types, such as DateTimeField, integer type IntegerField, and so on.
    You can view the documentation for all types built into Django:
    https://docs.djangoproject.com/en/2.2/ref/models/fields/#field-types
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Tag(models.Model): 
    """
    Tag is also relatively simple, just like Category.
    Again, we must inherit the models.Model class!
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):
    """
    The database table of the article is a little more complicated, mainly involving more fields.
    """

    # Articletitle
    title = models.CharField(max_length=70)

    # Article body, we used TextField.
    # CharField can be used to store short strings, but it may be a large text for the body of the article, so use TextField to store large text.
    body = models.TextField()

    # These two columns represent the creation time and last modification time of the article, and the field storing the time is of type DateTimeField.
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()

    # Article summary, there can be no article summary, but by default CharField requires that we must store data, otherwise it will report an error.
    # Specify the blank=True parameter value of CharField to allow null values.
    excerpt = models.CharField(max_length=200, blank=True)

    # This is classification and labeling. The model of classification and labeling has been defined above.
    # Here we associate the database table corresponding to the article with the database table corresponding to the category and label, but the association form is slightly different.
    # We stipulate that one article can only correspond to one category, but there can be multiple articles under one category, so we use ForeignKey, which is a one-to-many association relationship.
    # And since django 2.0, ForeignKey must pass an on_delete parameter to specify the behavior of the associated data when the associated data is deleted,
    # We assume here that when a category is deleted, all articles in that category are also deleted at the same time, so the models.CASCADE parameter is used, which means cascading deletion.
    # For tags, an article can have multiple tags, and there can be multiple articles under the same tag, so we use ManyToManyField to indicate that this is a many-to-many relationship.
    # At the same time, we stipulate that articles can have no tags, so we specify blank=True for tags.
    # If you don't know ForeignKey, ManyToManyField, please see the explanation in the tutorial, or refer to the official documentation:
    # https://docs.djangoproject.com/en/2.2/topics/db/models/#relationships
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, blank=True)

    # Article author, here User is imported from django.contrib.auth.models.
    # django.contrib.auth is Django's built-in application, which is specially used to handle the registration and login processes of website users. User is the user model that Django has written for us.
    # Here we associate the article with User through ForeignKey.
    # Because we stipulate that an article can only have one author, and an author may write multiple articles, this is a one-to-many relationship, similar to Category.
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title   