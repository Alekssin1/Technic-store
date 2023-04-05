from django import forms
from .models import CommentContent

class CommentForm(forms.ModelForm):
     
    text = forms.CharField(widget=forms.Textarea(
        attrs={"class": "text_of_comment", "placeholder": "Введіть коментар...", 
               "id": "text_input", "type": "text", "rows": "2"}), 
        label=""
        )
    
    class Meta:
        model = CommentContent
        fields = ['text']
        
    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['text'].required = False
