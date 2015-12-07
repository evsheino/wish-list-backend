from django.db import models
from django.contrib.auth.models import User
from model_utils.models import TimeStampedModel


class Category(models.Model):
    """ Represents the different types of gifts. """

    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Gift(TimeStampedModel):
    """ An item a user wishes to receive as a gift. """

    # The user that wishes to receive the gift
    user = models.ForeignKey(User, related_name='gifts')
    category = models.ForeignKey(Category, related_name='gifts')

    name = models.CharField(max_length=500)
    author = models.CharField(max_length=500)
    comment = models.CharField(max_length=1000, blank=True)

    # A link to an outside page with e.g. information regarding the item
    link = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return self.name


class Purchase(TimeStampedModel):
    """ Represents a purchase of a gift for a user by another user. """

    gift = models.ForeignKey(Gift, related_name='purchases')
    user = models.ForeignKey(User, related_name='purchases')
    comment = models.CharField(max_length=1000, blank=True)
