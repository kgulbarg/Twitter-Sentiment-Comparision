from django import forms
from django.utils.safestring import mark_safe

from django.contrib.admin.widgets import AdminDateWidget
from django.forms.fields import DateField


class PrDeForm(forms.Form):
    brand = forms.CharField(label = mark_safe('Brand'),widget=forms.TextInput(attrs={'placeholder': 'Mandatory'}))
    product = forms.CharField(label = mark_safe('Product'),widget=forms.TextInput(attrs={'placeholder': 'Mandatory'}))
    modelname1 = forms.CharField(label = mark_safe('Model 1'),widget=forms.TextInput(attrs={'placeholder': 'Mandatory'}))
    modelname2 = forms.CharField(label = mark_safe('Model 2'),widget=forms.TextInput(attrs={'placeholder': 'Mandatory'}))
    modelname3 = forms.CharField(label = mark_safe('Model 3'), required = False,widget=forms.TextInput(attrs={'placeholder': 'Optional'}))
    modelname4 = forms.CharField(label = mark_safe('Model 4'), required = False,widget=forms.TextInput(attrs={'placeholder': 'Optional'}))

class BrDeForm(forms.Form):
    product = forms.CharField(label = mark_safe('Product'),widget=forms.TextInput(attrs={'placeholder': 'Mandatory'}))
    brand1 = forms.CharField(label = mark_safe('Brand 1'),widget=forms.TextInput(attrs={'placeholder': 'Mandatory'}))
    brand2 = forms.CharField(label = mark_safe('Brand 2'),widget=forms.TextInput(attrs={'placeholder': 'Mandatory'}))
    brand3 = forms.CharField(label = mark_safe('Brand 3'), required = False,widget=forms.TextInput(attrs={'placeholder': 'Optional'}))
    brand4 = forms.CharField(label = mark_safe('Brand 4'), required = False,widget=forms.TextInput(attrs={'placeholder': 'Optional'}))


#    start_date = forms.DateTimeField(
#        #input_formats=['%d/%m/%Y'], 
#        widget= forms.SelectDateWidget(years=range(2009,2020)),
#        label = mark_safe('<br/><br/>Start')
#    )
#    end_date = forms.DateTimeField(
#        #input_formats=['%d/%m/%Y'], 
#        widget= forms.SelectDateWidget(years=range(2009,2020)),
#        label = mark_safe('<br/><br/>End')
#    )

    

"""
class PrDeForm(forms.ModelForm):
    brand = forms.CharField(label = 'Brand')
    product = forms.CharField(label = 'Product')
    modelname = forms.CharField(label = 'Model')
    class Meta:
        model = PrDe
        fields = '__all__'
        exclude = []


        def clean_date(self):
            start_date = self.cleaned_data['start_date']
        end_date = self.cleaned_data['end_date']
        if start_date > end_date :
            raise forms.ValidationError("Start date should be before end date.")
        return start_date, end_date
        """