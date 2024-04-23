

from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from studentorg.models import Organization, OrgMember  # Import OrgMembers
from studentorg.forms import OrganizationForm, OrgMembersForm  # Import OrgMembersForm
from django.urls import reverse_lazy

# Define your views here...


class HomePageView(ListView):
    model = Organization
    context_object_name = 'home'
    template_name =  "home.html"

class OrganizationList(ListView):
    model = Organization
    context_object_name = 'Organization'
    template_name = 'org_list.html'
    paginate_by = 5

class OrganizationCreateView(CreateView):
    model = Organization
    form_class = OrganizationForm
    template_name = 'org_add.html'
    success_url = reverse_lazy('organization-list')

class OrganizationUpdateView(UpdateView):
    model = Organization
    form_class = OrganizationForm
    template_name = 'org_edit.html'
    success_url = reverse_lazy('organization-list')

class OrganizationDeleteView(DeleteView):
    model = Organization
    template_name = 'org_del.html'
    success_url = reverse_lazy('organization-list')


class OrgMembersList(ListView):
    model = OrgMember
    context_object_name = 'OrgMember'
    template_name = 'org_list.html'
    paginate_by = 5

class OrgMembersCreateView(CreateView):
    model = OrgMember
    form_class = OrgMembersForm
    template_name = 'org_add.html'
    success_url = reverse_lazy('orgmember-list')

class OrgMembersUpdateView(UpdateView):
    model = OrgMember
    form_class = OrgMembersForm
    template_name = 'org_edit.html'
    success_url = reverse_lazy('orgmember-list')

class OrgMembersDeleteView(DeleteView):
    model = OrgMember
    template_name = 'org_del.html'
    success_url = reverse_lazy('orgmember-list')