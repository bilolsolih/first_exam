from django.db import models
from apps.common.models import BaseModel
from ckeditor.fields import RichTextField
from phonenumber_field.modelfields import PhoneNumberField
from django.utils import timezone
from . import choices


class Vacancy(BaseModel):
    title = models.CharField(max_length=256)
    location = models.CharField(max_length=256)
    experience = models.CharField(max_length=64)
    type = models.CharField(max_length=4, choices=choices.JOB_TYPE, default='full')
    description = RichTextField()

    class Meta:
        indexes = [
            models.Index(fields=['-created'])
        ]
        ordering = ['-created']

        verbose_name = 'Vacancy'
        verbose_name_plural = 'Vacancies'

    def __str__(self):
        return f"Vacancy by {self.company.title} Company"


class Company(BaseModel):
    title = models.CharField(max_length=256)
    location = models.CharField(max_length=256)
    phone_number = PhoneNumberField(region='UZ')

    vacancies = models.ForeignKey('jobhunt.Vacancy', related_name='company', on_delete=models.CASCADE)

    class Meta:
        indexes = [
            models.Index(fields=['title'])
        ]
        ordering = ['title']

        verbose_name = 'Company'
        verbose_name_plural = 'Companies'

    def __str__(self):
        return self.title


class Resume(BaseModel):
    first_name = models.CharField(max_length=128)
    middle_name = models.CharField(max_length=128, null=True, blank=True)
    last_name = models.CharField(max_length=128)
    birthdate = models.DateField(default=timezone.now)
    profession = models.CharField(max_length=256)
    experience = models.CharField(max_length=64)

    skills = RichTextField()

    class Meta:
        indexes = [
            models.Index(fields=['-created'])
        ]
        ordering = ['-created']

        verbose_name = 'Vacancy'
        verbose_name_plural = 'Vacancies'

    @property
    def get_fullname(self):
        return f"Resume by {self.first_name} {self.middle_name} {self.last_name}"

    def __str__(self):
        return self.get_fullname
