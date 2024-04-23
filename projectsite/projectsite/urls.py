from django.contrib import admin
from django.urls import path
from studentorg.views import HomePageView, OrganizationList, OrganizationCreateView, OrganizationUpdateView, OrganizationDeleteView
from studentorg.views import OrgMembersList, OrgMembersCreateView, OrgMembersUpdateView, OrgMembersDeleteView
from .views import FormsView 



urlpatterns = [
    path("admin/", admin.site.urls),
    path('', HomePageView.as_view(), name='home'),
    path('organization_list/', OrganizationList.as_view(), name='organization-list'),
    path('organization_list/add/', OrganizationCreateView.as_view(), name='organization-add'),  # Added trailing slash
    path('organization_list/<int:pk>/', OrganizationUpdateView.as_view(), name='organization-update'),
    path('organization_list/<int:pk>/delete/', OrganizationDeleteView.as_view(), name='organization-delete'),  # Added trailing slash
    path('orgmembers/', OrgMembersList.as_view(), name='orgmember-list'),
    path('orgmembers/add/', OrgMembersCreateView.as_view(), name='orgmember-add'),
    path('orgmembers/<int:pk>/edit/', OrgMembersUpdateView.as_view(), name='orgmember-edit'),
    path('orgmembers/<int:pk>/delete/', OrgMembersDeleteView.as_view(), name='orgmember-delete'),
    path('forms/', FormsView.as_view(), name='forms'),  # Use the FormsView to handle the forms.html page
    # other urls
]
