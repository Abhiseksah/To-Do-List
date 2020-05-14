from django.urls import path

from .import views

urlpatterns = [
    path('start',views.start,name='home'),
    path('delete/<int:id>/',views.delete,name='delete'),
    path('home',views.home,name='Home'),
   # path('editItem/<str:pk_test>/',views.dynamic,name='editItem')
    path('dynamic/<int:pk_test>/',views.dynamic,name='dynamic'),
    path('dynamic/<int:pk>/editSave',views.editSave,name='editsave'),

    path('mark/<int:my_pk>/',views.mark,name='mark'),
   # path('unmark/<int:pk_test>/',views.,name='dynamic'),
]
