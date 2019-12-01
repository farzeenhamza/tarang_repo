from django.contrib.auth.models import User
from django.http import HttpResponse
from django.views.generic import DetailView, FormView
from django.views.generic.base import TemplateView
from django_datatables_view.base_datatable_view import BaseDatatableView

from .forms import RegisterForm
from .models import Profile


class HomePageView(TemplateView):
    template_name = "home.html"


class UsersView(TemplateView):
    template_name = "all_users.html"


class CreateProfileView(FormView):
    template_name = 'profile_form.html'
    form_class = RegisterForm

    def form_valid(self, form):
        data = form.cleaned_data
        user = User.objects.create(username=data['username'],
                                   email=data['email'],
                                   password=data['password'],
                                   )
        Profile.objects.filter(id=user.id).update(age=data['age'], gender=data['gender'], college=data['college'],
                                                  mobile_number=data['mobile_number'], place=data['place'])
        return HttpResponse('Successfully Registered')


class DisplayDetailView(DetailView):
    model = Profile


class UserDataTableView(BaseDatatableView):
    model = Profile
    columns = ['user', 'age', 'gender', 'college', 'mobile_number', 'place']

    def render_column(self, row, column):
        # if column == 'Update/Edit':
        #     return '<button title="Update or Edit" type="button" \
        #     data-id="{0}" \
        #     class="btn btn-dark btn-sm update1 ffu" \
        #     data-toggle="modal" \
        #     data-target="" ><i class="fas fa-edit" ><b class="btn-txt"> EDIT</b></i></button>'.format(row.id)

        return super(UserDataTableView, self).render_column(row, column)

    # def filter_queryset(self, qs):
    #     qs = qs.filter(employee=None)
    #     search = self.request.GET.get('search[value]', None)
    #     if search:
    #         qs = qs.filter(
    #             Q(serial_number__istartswith=search) |
    #             Q(category__category__istartswith=search))
    #
    #     return qs
