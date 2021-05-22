# Задача на ORM
 
<p>
class City(models.Model):<br>
    name = models.CharField()<br>
 </p>
 
class Person(models.Model):<br>
    name = models.CharField()<br>
    city = models.ForeignKey(City)<br>
 
 
# Вывести список людей и городов где они живут?
# Вывести всех людей, живущих в городе N
# Вывести 5 городов с наибольшим населением, упорядочив по убыванию. 
 
 
class Event(models.Model):<br>
    start_date = models.DateTimeField()<br>
    end_date = models.DateTimeField()<br>
 
 
# Реализовать пагинацию с сортировкой по разнице дат
