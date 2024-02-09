from django.forms.widgets import ClearableFileInput
from django.utils.translation import gettext_lazy as _

class CustomClearableFileInput(ClearableFileInput):
    print("In widgets.py Class CustomClearableFileInput")
    clear_checkbox_label = _('Remove')
    initial_text = _('Current Image')
    input_text = _('')
    # DMcC HTML template doesnt seem to be picking up so have put it into the templates folder
    template_name = 'products/custom_clearable_file_input.html'
    print("how do i know if this widget has activated?")