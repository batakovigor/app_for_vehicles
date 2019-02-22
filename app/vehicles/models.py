from django.db import models
from django.contrib.auth.models import User

#from djoser.urls.base import User
class District(models.Model):
    """Модель справочника районов"""
    name = models.CharField(max_length=50,verbose_name="Район")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Район"
        verbose_name_plural = "Районы"

class TypeRequest(models.Model):
    """Модель справочника типы заявок"""
    name = models.CharField(max_length=50,verbose_name="Тип заявки")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Тип заявки"
        verbose_name_plural = "Типы заявок"

class ModelCar(models.Model):
    """Модель справочника модели АТС"""
    name = models.CharField(max_length=50,verbose_name="Марка АТС")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Марка АТС"
        verbose_name_plural = "Марки АТС"

class TypeCar(models.Model):
    """Модель справочника типов АТС"""
    name = models.CharField(max_length=50,verbose_name="Тип АТС")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Тип АТС"
        verbose_name_plural = "Типы АТС"

class Car(models.Model):
    """Модель справочника автомобилей для заказа"""
    car_model = models.ForeignKey(ModelCar, related_name='car_model', verbose_name="Марка АТС", on_delete=models.CASCADE)
    gos_nomer = models.CharField(max_length=6,verbose_name="Гос.номер")
    type_car = models.ForeignKey(TypeCar, related_name='type_car', verbose_name="Тип АТС", on_delete=models.CASCADE)
    district = models.ForeignKey(District, related_name='district', verbose_name="Район",on_delete=models.CASCADE)

    def __str__(self):
        """
        String for representing the Model object.
        """
        # return '%s (%s)' % (self.id,self.book.title)
        return '{0} ({1})'.format(self.car_model.name, self.gos_nomer)

    class Meta:
        verbose_name = "Автомобиль"
        verbose_name_plural = "Автомобили"


class Department(models.Model):
    """Модель справочника подразделений"""
    name = models.CharField(max_length=50, verbose_name="Подразделение")


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Подразделение"
        verbose_name_plural = "Подразделения"

class Requests(models.Model):
    """Модель заявок на автотранспорт"""
    type_request = models.ForeignKey(TypeRequest, verbose_name="Тип заявки", on_delete=models.CASCADE)
    car = models.ForeignKey(Car, verbose_name="Автомобиль", on_delete=models.CASCADE)
    department = models.ForeignKey(Department, verbose_name="Подразделение(я)", related_name="departments", on_delete=models.CASCADE)
    date_request = models.DateField("Дата заявки")
    time_start_request = models.TimeField("Время подачи автомобиля")
    time_end_request = models.TimeField("Длительность использования")
    description = models.TextField(help_text="Пункт назначения, место подачи АТС, вид перевозки,цель поездки, характеристика груза, кол-во людей (указывать обязательно)")
    comment = models.TextField(help_text="Примечания, Ф.И.О., номера удостоверений, дату проверки знаний, ответственных,стропальщиков и расстояние до крайнего провода ЛЭП(указывать обязательно)")
    creater = models.ForeignKey(User, verbose_name="Автор", on_delete=models.CASCADE)
    date_creater = models.DateTimeField("Дата создания", auto_now_add=True)


    REQUEST_STATUS = (
        ('n', 'новая'),
        ('c', 'рассмотрение'),
        ('r', 'отклонена'),
        ('a', 'согласована'),
    )

    status = models.CharField(max_length=1, choices=REQUEST_STATUS, blank=True, default='n', help_text='Состояние заявки')

    def __str__(self):
        """
        String for representing the Model object.
        """
        # return '%s (%s)' % (self.id,self.book.title)
        return '{0} ({1} - {2})'.format(self.type_request.name, self.car.car_model, self.car.gos_nomer)

    class Meta:
        verbose_name = "Заявка на автотранспорт"
        verbose_name_plural = "Заявки на автотранспорт"
        ordering = ('date_creater',)