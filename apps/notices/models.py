from django.db import models
from apps.common.models import BaseModel


class Notice(BaseModel):
    user = models.ForeignKey('auth.User', related_name='notices', on_delete=models.SET_NULL, null=True)
    car_photo = models.ImageField(upload_to='images/notices/cars/%Y/%m/%d/', blank=True, null=True)
    brand = models.ForeignKey('notices.Brand', related_name='notices', on_delete=models.SET_NULL, null=True)
    model = models.ForeignKey('notices.CarModel', related_name='notices', on_delete=models.SET_NULL, null=True)
    price = models.DecimalField(max_digits=20, decimal_places=2, default=0)

    class Meta:
        verbose_name = 'Notice'
        verbose_name_plural = 'Notices'

    @property
    def get_average_price(self):
        notices = Notice.objects.filter(brand=self.brand, model=self.model).exclude(id=self.id)
        average_price = 0
        if notices:
            for notice in notices:
                average_price += notice.price
            average_price = (average_price + self.price) / (notices.count() + 1)
            return {'average': average_price}
        else:
            return {'average': self.price}

    @property
    def get_difference(self):
        percentage = self.price * 100 / self.get_average_price['average']
        return {'percentage': percentage, 'difference': self.price - self.get_average_price['average']}


class Brand(BaseModel):
    title = models.CharField(max_length=128)
    logo = models.ImageField(upload_to='images/notices/brand_logos/%Y/%m/%d/', null=True, blank=True)

    class Meta:
        verbose_name = 'Brand'
        verbose_name_plural = 'Brands'

    def __str__(self):
        return self.title


class CarModel(BaseModel):
    title = models.CharField(max_length=128)

    class Meta:
        verbose_name = 'Car model'
        verbose_name_plural = 'Car models'

    def __str__(self):
        return self.title

# Create your models here.
