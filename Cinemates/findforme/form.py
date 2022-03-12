from django import forms

class FormFindForMe(forms.Form):
    usercategory = forms.CharField(max_length=100)

    def __init__(self,user_category):
        self.usercategory =user_category