from django.contrib import admin
from django.urls import path,include
from emp_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='home'),
    path('add_emp/',views.add_emp,name='add_emp'),
    path('delete_emp/<int:emp_id>/',views.delete_emp,name='delete_emp'),
    path('update_emp/<int:emp_id>/',views.update_emp,name='update_emp'),
    path('do_update_emp/<int:emp_id>/',views.do_update_emp,name='do_update_emp'),
    path('more/',views.more,name='more'),
]
