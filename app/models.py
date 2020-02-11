from django.db import models


class District(models.Model):
    """Table to store District details."""

    name = models.CharField(max_length=200)


class Taluk(models.Model):
    """Table to store District details."""

    name = models.CharField(max_length=200)
    district = models.ForeignKey(
        District,
        on_delete=models.CASCADE,
        related_name="taluks")


class College(models.Model):
    """Table to store District details."""

    name = models.CharField(max_length=200)
    taluk = models.ForeignKey(
        Taluk,
        on_delete=models.CASCADE,
        related_name="colleges")


class BloodGroup(models.Model):
    """Table to store blood group details."""

    group = models.CharField(max_length=10)


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


class Donation(models.Model):
    """Table to store District details."""

    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name="donation_history")
    donated_date = models.DateField(auto_now=True)
