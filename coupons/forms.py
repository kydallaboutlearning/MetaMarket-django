from django import forms
from .models import Coupon
from django.utils.translation import gettext_lazy as _

class CouponApplyForm(forms.Form):
    code = forms.CharField(label=_('Coupon'))


class Amount_Choice_form(forms.Form):
    choices = [
        ('Yes', 'Yes'),
        ('No', 'No'),
        ]
    choice = forms.CharField(label='Choose an Option', widget=forms.RadioSelect(choices=choices))

class Amount_form(forms.ModelForm):
    class Meta:
        model = Coupon
        fields = ('amount_available',)


