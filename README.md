# Задача на ORM
 
class City(models.Model):
    name = models.CharField()
 
 
class Person(models.Model):
    name = models.CharField()
    city = models.ForeignKey(City)
 
 
# Вывести список людей и городов где они живут?
# Вывести всех людей, живущих в городе N
# Вывести 5 городов с наибольшим населением, упорядочив по убыванию. 
 
 
class Event(models.Model):
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
 
 
# Реализовать пагинацию с сортировкой по разнице дат
