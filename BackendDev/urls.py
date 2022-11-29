"""BackendDev URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from BackendDev import views as main_views
from data import views as data_views
from rest_framework import routers


# router = routers.DefaultRouter()
# #access registered ViewSets: localhost:8000/api/[NAME]
# router.register(r'Departments', data_views.DepartmentViewSet) 
# router.register(r'Majors', data_views.MajorViewSet)
# router.register(r'Minors', data_views.MinorViewSet) 
# router.register(r'Students', data_views.StudentViewSet) 
# router.register(r'Professors', data_views.ProfessorViewSet) 
# router.register(r'AdminAssistants', data_views.AdminAssistantViewSet) 
# router.register(r'Courses', data_views.CourseViewSet) 
# router.register(r'HighImpactExperiences', data_views.HighImpactExperienceViewSet) 
# router.register(r'Events', data_views.EventViewSet)


# https://stackoverflow.com/questions/53989959/how-to-allow-post-for-update-action-in-django-rest-framework

#post (create) -- requires add
#put, patch (updates) -- requires change
#delete (destroy) -- requires delete
#get (list, retrieve) -- requires view ..(?)

#maybe check perms here -- URL perms?
student_list = data_views.StudentViewSet.as_view({'get':'list'})
student_create = data_views.StudentViewSet.as_view({'post':'create'})
student_specific = data_views.StudentViewSet.as_view({ #pk 
    'get':'retrieve',
    'put':'update',
    'patch':'partial_update',
    'delete':'destroy'
})

prof_list = data_views.ProfessorViewSet.as_view({'get':'list'})
prof_create = data_views.ProfessorViewSet.as_view({'post':'create'})
prof_specific = data_views.ProfessorViewSet.as_view({
    'get':'retrieve',
    'put':'update',
    'patch':'partial_update',
    'delete':'destroy'
})

urlpatterns = [
    path('admin/', admin.site.urls), #access: localhost:8000/admin/
    path('', main_views.index, name='index'), #access: localhost:8000/
    path('HIEs-display/', main_views.HIEs_display, name='HIE-display'),
    path('HIEs-raw/', main_views.HIEs_raw, name='HIE-raw'),
    path('files/', main_views.files, name='files'), #access: localhost:8000/files/
    path('login/', main_views.auth, name='auth'),
    # path('api/', include(router.urls)) #access: localhost:8000/api/[router.url]

    path('api/', data_views.api, name='api'), #access: localhost:8000/api/
    
    path('api/Student/register/', student_create, name='student-create'),
    path('api/Student/list/', student_list, name='student-list'),
    path('api/Student/<int:pk>/', student_specific, name='student-specific'),
    
    path('api/Professor/register/', prof_create, name='prof-create'),
    path('api/Professor/list/', prof_list, name='prof-list'),
    path('api/Professor/<int:pk>/', prof_specific, name='prof-specific'),
    # path()
]
