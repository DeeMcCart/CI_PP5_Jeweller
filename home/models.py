from django.db import models

# Create your models here.

ABOUT_TYPE = [
    ('ABOUT', 'About Section'),
    ('FAQ', 'Frequently Asked Questions'),
    ('ENQUIRY', 'Customer Enquiry Text'),
]


class AboutSection(models.Model):
    section = models.CharField(max_length=7, choices=ABOUT_TYPE,
                               default='ABOUT')
    disp_seq = models.IntegerField(default=10)
    hide_display = models.BooleanField(default=False)
    section_title = models.CharField(max_length=50, null=False, blank=False)

    class Meta:
        """ returns an overall list """
        ordering = ['disp_seq']

    def __str__(self):
        return (f'{self.section} seq{self.disp_seq} '
                + f'Title {self.section_title} hide: {self.hide_display}')


class AboutText(models.Model):
    section = models.ForeignKey(AboutSection,
                                on_delete=models.CASCADE,
                                related_name="about_section")
    disp_seq = models.IntegerField(default=10)
    hide_display = models.BooleanField(default=False)
    text_title = models.CharField(max_length=50, null=False, blank=False)
    text_body = models.TextField(blank=True)

    class Meta:
        """ returns an overall list """
        ordering = ['disp_seq']

    def __str__(self):
        return f'Seq {self.disp_seq} Title {self.text_title}'
