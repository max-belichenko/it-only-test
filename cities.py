# Задача на ORM

class City(models.Model):
    name = models.CharField()
 
 
class Person(models.Model):
    name = models.CharField()
    city = models.ForeignKey(City)
 

# Вывести список людей и городов где они живут?
for item in Person.objects.select_related('city').all():
    print(f'{item.name} from {item.city.name}')

# Вывести всех людей, живущих в городе N
for item in Person.objects.filter(city__name=N).values():
    print(f'{item["name"]} lives in {N} city')
  
# Вывести 5 городов с наибольшим населением, упорядочив по убыванию. 
from django.db.models import Count


cities = City.objects.annotate(person_count=Count('person'))

for city in cities.order_by('-person_count')[:5]:
    print(city.name, city.person_count)
  




class Event(models.Model):
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
 
 
# Реализовать пагинацию с сортировкой по разнице дат
from django.core.paginator import Paginator


events = Event.objects.annotate(date_diff=F('end_date')-F('start_date')).order_by('-date_diff')
objects_per_view = 3
paginator = Paginator(events, objects_per_view)

for page_number in paginator.page_range:
    page = paginator.page(page_number)
	print(page)
	for object in page.object_list:
        print(object.start_date, object.end_date, object.date_diff)
