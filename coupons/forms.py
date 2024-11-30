from django import forms
from .models import Coupon
from django.utils.translation import gettext_lazy as _

class CouponApplyForm(forms.Form):
    code = forms.CharField(label=_('Coupon'))


class Amount_Choice_form(forms.Form):
    #saving a variable for the translation
    trans_yes  =  _('Yes')
    trans_no  =  _('No')



    choices = [
        (trans_yes, trans_yes),
        (trans_no, trans_no),
        ]
    choice = forms.CharField(label=_('Choose an Option'), widget=forms.RadioSelect(choices=choices))

class Amount_form(forms.ModelForm):
    class Meta:
        model = Coupon
        fields = ('amount_available',)


