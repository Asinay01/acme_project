from django.db import models
# for IntegerField
# from django.core.validators import MinValueValidator, MaxValueValidator
# validators=[MinValueValidator(10), MaxValueValidator(100)],


class Birthday(models.Model):
    first_name = models.CharField('Имя', max_length=20)
    last_name = models.CharField(
        'Фамилия', blank=True, help_text='Необязательное поле', max_length=20
    )
    birthday = models.DateField('Дата рождения')
