from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from employees.forms import FormEmployee
from employees.models import Employee


class EmployeeView(ListView):
    template_name = 'index.html'
    queryset = Employee.objects.order_by('-id')
    context_object_name = 'employees'
    paginate_by = 5


class EmployeeCreateView(CreateView):
    form_class = FormEmployee
    template_name = 'create.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        if form.is_valid():
            form.save()
        return super().form_valid(form)


class EmployeeUpdateView(UpdateView):
    form_class = FormEmployee
    queryset = Employee.objects.all()
    template_name = 'update.html'
    # context_object_name = 'employee'
    success_url = reverse_lazy('index')


class EmployeeDeleteView(DeleteView):
    model = Employee
    template_name = 'delete.html'
    success_url = reverse_lazy('index')
