#  DMcC 31/01/24 this will need more work to maintain products and display category 1-6 titles and range of values
#

from django import forms
from .models import Product, Category, Cat1, Cat2, Cat3, Cat4
from .widgets import CustomClearableFileInput


class ProductForm(forms.ModelForm):
    
    class Meta:
        model = Product
        fields = '__all__'
    

    preimage = forms.ImageField()
    if (preimage):
        print('In ProductForm, Pre-Image exists', preimage)


    # DMcC 09/02/24:  Apply our lovely widget to improve clunky apperance of image
    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)
    if (image):
        print('In ProductForm, Image exists', image)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        # permit only the friendly names for the choices in product category
        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
