from django import forms
from product.models import Product


class ProductForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for visible in self.visible_fields():
            visible.required = True
            visible.field.widget.attrs['class'] = 'form-control'

        self.fields['user'].required = False

    class Meta:
        model = Product
        fields = "__all__"
