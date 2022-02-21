from django import forms

class FeedbackForm(forms.Form):
    title = forms.CharField(label='Title', max_length=50,widget=forms.TimeInput(attrs={'class':'form-control'}))
    subject = forms.CharField(label='Subject Description',max_length=200, widget=forms.Textarea(attrs={'class':'form-control'}))

