from django import forms
from .models import Package_ordered


class PackageOrderedForm(forms.ModelForm):
    class Meta:
        model = Package_ordered
        fields = ('customer_name', 'customer_email',
                  'phone_number', 'postcode',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'customer_name': 'Customer Name',
            'customer_email': 'Customer Email Address',
            'phone_number': 'Phone Number',
            'postcode': 'postcode'
        }
        # taken from b/a project
        self.fields['customer_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'  # css class
            self.fields[field].label = False