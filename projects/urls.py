from django.urls import path

from projects.views import ProjectListView, ProjectDetailView

urlpatterns = [
    path("", ProjectListView.as_view(), name="projects_list"),
    path("<int:pk>/", ProjectDetailView.as_view(), name="show_project"),
]
