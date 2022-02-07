from django import forms

class Searchform(forms.Form):
    usersearch = forms.CharField(max_length=100)

    def __init__(self,user_input):
        self.usersearch =user_input
