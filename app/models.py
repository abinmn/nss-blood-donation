from django.contrib.auth.models import User

from django.db import models


class District(models.Model):
    """Table to store District details."""

    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Taluk(models.Model):
    """Table to store District details."""

    name = models.CharField(max_length=200)
    district = models.ForeignKey(
        District,
        on_delete=models.CASCADE,
        related_name="taluks")

    def __str__(self):
        return self.name


class College(models.Model):
    """Table to store District details."""

    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    taluk = models.ForeignKey(
        Taluk,
        on_delete=models.CASCADE,
        related_name="colleges")
    

    def blood_group_count(self, group_id):
        return self.students.filter(blood_group=group_id).count()

    def __str__(self):
        return self.name


class BloodGroup(models.Model):
    """Table to store blood group details."""

    group = models.CharField(max_length=10)

    def __str__(self):
        return self.group


class Student(models.Model):
    """Table to store student details."""

    name = models.CharField(max_length=300)
    student_class = models.CharField(max_length=10)
    mobile_number = models.BigIntegerField()
    email = models.EmailField()
    passout_year = models.IntegerField()
    height = models.IntegerField()
    weight = models.IntegerField()
    blood_group = models.ForeignKey(
        BloodGroup,
        on_delete=models.CASCADE,
        related_name="members")
    college = models.ForeignKey(
        College,
        on_delete=models.CASCADE,
        related_name="students"
    )

    def __str__(self):
        return f"{self.name} - {self.college}"


class Donation(models.Model):
    """Table to store District details."""

    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name="donation_history")
    donated_date = models.DateField(auto_now=True)


class VolunteerProfile(models.Model):
    """Table to store District details."""

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    college = models.ForeignKey(
        College,
        on_delete=models.CASCADE,
        related_name="volunteers")
