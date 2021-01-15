from .import views
from django.urls import path

app_name = 'foodtrucks'

urlpatterns = [
    path('',views.homepage,name='homepage'),
    path('all/trucks/',views.alltrucks,name='alltrucks'),
    path('add/truck/',views.addtruck,name='addtruck'), 
    path('edit/truck/<int:truck_id>/',views.edit,name='edit'),   
    path('delete/truck/<int:truck_id>',views.deletetruck,name='deletetruck'),
]