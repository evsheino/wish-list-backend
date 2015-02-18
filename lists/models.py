from django.db import models
from django.contrib.auth.models import User
from model_utils import Choices
from model_utils.models import TimeStampedModel
from model_utils.managers import InheritanceManager

class Gift(TimeStampedModel):
    """ An item a user wishes to receive as a gift. """

    # The user that wishes to receive the gift
    user = models.ForeignKey(User)
    category = models.ForeignKey(Category)

    name = models.CharField(max_length=500)
    author = models.CharField(max_length=500)
    comment = models.CharField(max_length=1000)

    # A link to an outside page with e.g. information regarding the gift
    link = models.CharField(max_length=500)


class Purchase(TimeStampedModel)
    """ Represents a purchase of a gift for a user by another user. """

    gift = models.ForeignKey(Gift)
    user = models.ForeignKey(User)
    comment = models.CharField(max_length=1000)


class Category(models.Model):
    """ Represents the different types of gifts. """

    name = CharField(max_length=50)

