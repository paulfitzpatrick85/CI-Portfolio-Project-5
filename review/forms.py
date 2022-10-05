from .models import Review
from django import forms


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('customer_name',
                  'customer_email',
                  'customer_password',
                  'customer_review',)
                  