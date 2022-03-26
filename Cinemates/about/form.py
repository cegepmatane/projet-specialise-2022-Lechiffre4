from django import forms

class ContactForm(forms.Form):
    usersname = forms.CharField(max_length=100)
    usersmail = forms.EmailField()
    usersmessage = forms.CharField(widget=forms.Textarea)

    def __init__(self,user_input,user_input2,user_input3):
        self.username =user_input
        self.usersmail =user_input2
        self.usersmessage =user_input3
