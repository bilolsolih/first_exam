from django.db import models
from apps.common.models import BaseModel
from ckeditor.fields import RichTextField
from django.core.validators import MinValueValidator, MaxValueValidator
from rest_framework.response import Response


class Service(BaseModel):
    title = models.CharField(max_length=128)
    logo = models.ImageField(upload_to='images/services/logos/%Y/%m/%d/', null=True, blank=True)

    # feedbacks
    # products

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'

    @property
    def get_rating(self):
        one, two, three, four, five, final = 0, 0, 0, 0, 0, 0
        all_feedbacks = self.feedbacks.all()
        if all_feedbacks:
            for feedback in all_feedbacks:
                final += feedback.rating
                if feedback.rating == 1:
                    one += 1
                elif feedback.rating == 2:
                    two += 1
                elif feedback.rating == 3:
                    three += 1
                elif feedback.rating == 4:
                    four += 1
                elif feedback.rating == 5:
                    five += 1
                else:
                    raise ValueError('Rating should be any integer between 1 and 5!')
            response = {'overall': final / all_feedbacks.count(), 'one': one, 'two': two, 'three': three, 'four': four, 'five': five}
            return response
        else:
            return {'overall': 'not rated yet'}

    def __str__(self):
        return self.title


class Product(BaseModel):
    service = models.ForeignKey('services.Service', related_name='products', on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    description = RichTextField()
    price = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    discount = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    @property
    def get_price(self):
        return self.price - (self.price / 100 * self.discount)

    def __str__(self):
        return f"{self.title} by {self.service.title}"


class Feedback(BaseModel):
    user = models.ForeignKey('auth.User', related_name='feedbacks', on_delete=models.SET_NULL, null=True)
    service = models.ForeignKey('services.Service', related_name='feedbacks', on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(5)])
    comment = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = 'Feedback'
        verbose_name_plural = 'Feedbacks'

        indexes = [
            models.Index(fields=['rating']),
            models.Index(fields=['created']),
        ]

        ordering = ['created']

    def __str__(self):
        return f"Feedback by {self.user.get_full_name()}"
