from django.forms.widgets import ClearableFileInput
from django.utils.translation import gettext_lazy as _


class CustomClearableFileInput(ClearableFileInput):
    clear_checkbox_label = _('Remove')
    initial_text = _('Current Image')
    input_text = _('')
    # DMcC HTML template not picking up so put it into the templates folder
    template_name = 'profiles/custom_clearable_file_input.html'
