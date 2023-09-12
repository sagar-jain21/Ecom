from django.db import models
from authentication.models import User
from product.models import Product
import uuid


class Cart(models.Model):

    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, blank=True)
