from django import forms
from .models import News
import re


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'content', 'is_public', 'category']
        widgets = {
            'title': forms.TextInput(attrs={'class': "form-control"}),
            'content': forms.Textarea(attrs={'class': "form-control", 'rows': 5}),
            'category': forms.Select(attrs={'class': "form-control"}),
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if re.match(r'\d', title):
            raise forms.ValidationError('Название не должно начинаться с цифры!')
        return  title
