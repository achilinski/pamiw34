from django import forms

class BookForm(forms.Form):
    title = forms.CharField(label='Title', max_length=100)
    author = forms.CharField(label='Author', max_length=100)
    date_of_publishing = forms.DateField(label='Date of Publishing', widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    CATEGORY_CHOICES = [
        ('comedy', 'Comedy'),
        ('drama', 'Drama'),
        ('educational', 'Educational'),
        ('thriller', 'Thriller'),
    ]
    category = forms.ChoiceField(label='Category', choices=CATEGORY_CHOICES)
    rating = forms.FloatField(label='Rating', min_value=1, max_value=5)

