from django import forms
from django.contrib.auth.models import User
from . import models
from .models import answer
# for admin


class AdminSigupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password']


# for student related form
class StudentUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password']


class StudentExtraForm(forms.ModelForm):
    class Meta:
        model = models.StudentExtra
        fields = ['roll', 'cl', 'mobile', 'fee', 'status']


# for teacher related form
class TeacherUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password']


class TeacherExtraForm(forms.ModelForm):
    class Meta:
        model = models.TeacherExtra
        fields = ['salary', 'mobile', 'status']


# for Attendance related form
presence_choices = (('Present', 'Present'), ('Absent', 'Absent'))


class AttendanceForm(forms.Form):
    present_status = forms.ChoiceField(choices=presence_choices)
    date = forms.DateField()


class AskDateForm(forms.Form):
    date = forms.DateField()


class AskDateForm(forms.Form):
    date = forms.DateField()


# for feedback form
RATING_CHOICES = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')
)


class feedback(forms.ModelForm):
    rating1 = forms.ChoiceField(choices=RATING_CHOICES)
    rating2 = forms.ChoiceField(choices=RATING_CHOICES)
    rating3 = forms.ChoiceField(choices=RATING_CHOICES)
    suggestions = forms.CharField(widget=forms.Textarea(attrs={"rows": "5"}))

    class Meta:
        model = models.feedback
        fields = ['rating1', 'rating2', 'rating3', 'suggestions']

# for quiz


class AnswerForm(forms.ModelForm):
    class Meta:
        model = answer
        fields = ['text']

    # for notice related form


class NoticeForm(forms.ModelForm):
    class Meta:
        model = models.Notice
        fields = '__all__'


# for contact us page
class ContactusForm(forms.Form):
    Name = forms.CharField(max_length=30)
    Email = forms.EmailField()
    Message = forms.CharField(
        max_length=500, widget=forms.Textarea(attrs={'rows': 3, 'cols': 30}))
