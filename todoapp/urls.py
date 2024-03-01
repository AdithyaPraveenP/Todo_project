from django.urls import path

from .import views

urlpatterns = [
    path("",views.home,name='home'),
    # path('add/',views.add,name='add'),
    # path('detail/',views.detail,name='detail'),
    path('test/',views.test,name="test"),
    path('delete/<int:taskid>/',views.delete,name='delete'),
    path('update/<int:id>/',views.update,name='update'),
    path('cbvhome/',views.Tasklistview.as_view(),name='cbvhome'),
    path('cbvdetail/<int:pk>/',views.TaskDetailview.as_view(),name="cbvdetail"),
    path('cbvupdate/<int:pk>/',views.TaskUpdateView.as_view(),name="cbvupdate"),
    path('cbvdelete/<int:pk>/',views.TaskDeleteView.as_view(),name="cbvdelete"),

]