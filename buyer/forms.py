from django.forms import ModelForm
from buyer.models import Cart


class CartForm(ModelForm):

    class Meta:
        model = Cart
        fields = "__all__"
