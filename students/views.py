from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login

class StudentRegistrationView(CreateView):
    template_name = 'students/student/registration.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('student_course_list')

    def form_valid(self, form):
        # Save the new user
        result = super().form_valid(form)
        # Get cleaned data from the form
        cd = form.cleaned_data
        # Authenticate the user
        user = authenticate(username=cd['username'], password=cd['password1'])
        if user is not None:
            # Log the user in
            login(self.request, user)
        return result

from django.views.generic.edit import FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .forms import CourseEnrollForm

class StudentEnrollCourseView(LoginRequiredMixin, FormView):
    form_class = CourseEnrollForm
    course = None

    def form_valid(self, form):
        self.course = form.cleaned_data['course']
        self.course.students.add(self.request.user)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('student_course_detail', args=[self.course.id])


from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from courses.models import Course

class StudentCourseListView(LoginRequiredMixin, ListView):
    model = Course
    template_name = 'students/course/list.html'

    def get_queryset(self):
        qs = super().get_queryset()
        # Filter courses where the current user is a student
        return qs.filter(students=self.request.user)
    


from django.views.generic.detail import DetailView

class StudentCourseDetailView(DetailView):
    model = Course
    template_name = 'students/course/detail.html'

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(students__in=[self.request.user])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        course = self.get_object()
        
        if 'module_id' in self.kwargs:
            # get the current module
            context['module'] = course.modules.get(id=self.kwargs['module_id'])
        else:
            # get the first module
            context['module'] = course.modules.all().first()  # safer than [0] if empty

        return context

