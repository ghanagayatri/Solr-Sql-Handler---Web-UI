from django import forms

# our new form
class SqlForm(forms.Form):
    query = forms.CharField(
        required=True,
        widget=forms.Textarea
    )
