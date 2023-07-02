from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class TeacherExtra(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    salary = models.PositiveIntegerField(null=False)
    joindate = models.DateField(auto_now_add=True)
    mobile = models.CharField(max_length=40)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.user.first_name

    @property
    def get_id(self):
        return self.user.id

    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name


classes = [('Standard 1', 'Standard 1'), ('Standard 2', 'Standard 2'), ('Standard 3', 'Standard 3'),
           ('Standard 4', 'Standard 4'), ('Standard 5', 'Standard 5'), ('Standard 6', 'Standard 6'), ('Standard 7', 'Standard 7'), ('Standard 8', 'Standard 8'), ('Standard 9', 'Standard 9'), ('Standard 10', 'Standard 10')]


class StudentExtra(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    roll = models.CharField(max_length=10)
    mobile = models.CharField(max_length=40, null=True)
    fee = models.PositiveIntegerField(null=True)
    cl = models.CharField(max_length=100, choices=classes,
                          default='Standard 1')
    status = models.BooleanField(default=False)

    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name

    @property
    def get_id(self):
        return self.user.id

    def __str__(self):
        return self.user.first_name


class Attendance(models.Model):
    roll = models.CharField(max_length=10, null=True)
    date = models.DateField()
    cl = models.CharField(max_length=10)
    present_status = models.CharField(max_length=10)


class Notice(models.Model):
    date = models.DateField(auto_now=True)
    by = models.CharField(max_length=20, null=True, default='school')
    message = models.CharField(max_length=500)


RATING_CHOICES = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')
)


class feedback(models.Model):
    user = models.OneToOneField(
        User, default=None, null=True, on_delete=models.CASCADE)
    rating1 = models.CharField(choices=RATING_CHOICES, max_length=500)
    rating2 = models.CharField(choices=RATING_CHOICES, max_length=500)
    rating3 = models.CharField(choices=RATING_CHOICES, max_length=500)
    suggestions = models.CharField(max_length=500)

    class Meta:
        verbose_name = "feedback"
        verbose_name_plural = "feedbacks"

# quiz


class question(models.Model):
    text = models.CharField(max_length=255)

    def __str__(self):
        return self.text


class answer(models.Model):
    question = models.ForeignKey(question, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    option = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.text
