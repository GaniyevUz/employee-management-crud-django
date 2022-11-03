from django.urls import path

from employees.views import EmployeeView, EmployeeCreateView, EmployeeUpdateView, EmployeeDeleteView

urlpatterns = [
    path('', EmployeeView.as_view(), name='index'),
    path('page/<int:page>', EmployeeView.as_view(), name='page'),
    path('create/', EmployeeCreateView.as_view(), name='create'),
    path('update/<int:pk>', EmployeeUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', EmployeeDeleteView.as_view(), name='delete')
]
