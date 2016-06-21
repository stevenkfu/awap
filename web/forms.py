from django import forms
from web.models import Team

class TeamForm(forms.ModelForm):

    class Meta:
        model = Team
        fields = ['name', 'password',
                  'member_1', 'member_2', 'member_3', 'member_4',
                  'email_1', 'email_2', 'email_3', 'email_4',
                  'size_1', 'size_2', 'size_3', 'size_4', 'diet']
        exclude = ['score', 'code', 'last_login']

    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
                                        'class': 'form-control',
                                        'placeholder': 'Team Name',
                                         }))
    password = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Be sure to remember this as other team members will need this to log in to the team'}))
    member_1 = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'This should be your name',}))
    member_2 = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Optional'}))
    member_3 = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Optional'}))
    member_4 = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Optional'}))
    email_1 = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'This should be your email',}))
    email_2 = forms.EmailField(required=False, widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Optional'}))
    email_3 = forms.EmailField(required=False, widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Optional'}))
    email_4 = forms.EmailField(required=False, widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Optional'}))
    SHIRT_SIZES = (
        ('', 'None'),
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        )
    size_1 = forms.CharField(widget=forms.Select(choices=SHIRT_SIZES, attrs={'class': 'form-control',}), required=False)
    size_2 = forms.CharField(widget=forms.Select(choices=SHIRT_SIZES, attrs={'class': 'form-control',}), required=False)
    size_3 = forms.CharField(widget=forms.Select(choices=SHIRT_SIZES, attrs={'class': 'form-control',}), required=False)
    size_4 = forms.CharField(widget=forms.Select(choices=SHIRT_SIZES, attrs={'class': 'form-control',}), required=False)
    diet = forms.CharField(max_length=1000, widget=forms.Textarea(attrs={'class': 'form-control'}), required=False)


class ManageTeamForm(TeamForm):

    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Team Name',
        'readonly': 'readonly'}))
