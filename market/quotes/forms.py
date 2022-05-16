from django import forms  
from quotes.models import List
from.models import Stock

class ListForm(forms.ModelForm):
    class Meta:
        model = List
        fields = "__all__"
        
    def clean_field(self):
        item = self.cleaned_data['item']
        if len(item) < 3:
            raise forms.ValidationError("Need at least three characters")
        return item

from.models import Stock

class StockForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ["ticker"]
    