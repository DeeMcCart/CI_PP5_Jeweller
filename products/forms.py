from django import forms
from .models import Product, Category, Review
from .widgets import CustomClearableFileInput


class ProductForm(forms.ModelForm):
    """ Used to hold the product maintenance fields """
    class Meta:
        model = Product
        fields = '__all__'

    # DMcC 09/02/24:  Apply widget to improve clunky apperance of image
    image = forms.ImageField(label='Image', required=False,
                             widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        # permit only the friendly names for the choices in product category
        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'


class ReviewForm(forms.ModelForm):
    rating = forms.IntegerField(required=True)  

    class Meta:
        model = Review
        fields = (
            'user_profile',
            'product',
            'rating',
            'title',
            'body',
                )
