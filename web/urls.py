from django.urls import path
from . import views
from django.urls import path

urlpatterns = [
    path('home/',views.home,name='home'),
    path('download/', views.my_view, name='download_pdf'),
    path("", views.index, name="index"),
    path("teams/<str:pk>/", views.teams, name="teams"),
    path(
        "course_outline/<str:pk>/<str:sk>/", views.course_outline, name="course_outline"
    ),
    path(
        "record_of_invention/<str:pk>/<str:sk>/",
        views.record_of_invention,
        name="record_of_invention",
    ),
    path(
        "statement_of_originality/<str:pk>/<str:sk>/",
        views.statement_of_originality,
        name="statement_of_originality",
    ),
    path("flowchart/<str:pk>/<str:sk>/", views.flowchart, name="flowchart"),
    path("step_1/<str:pk>/<str:sk>/", views.step_1, name="step_1"),
    path("step_2/<str:pk>/<str:sk>/", views.step_2, name="step_2"),
    path("step_3/<str:pk>/<str:sk>/", views.step_3, name="step_3"),
    path("step_4/<str:pk>/<str:sk>/", views.step_4, name="step_4"),
    path("step_5/<str:pk>/<str:sk>/", views.step_5, name="step_5"),
    path("step_6/<str:pk>/<str:sk>/", views.step_6, name="step_6"),
    path("step_7/<str:pk>/<str:sk>/", views.step_7, name="step_7"),
    path("step_8/<str:pk>/<str:sk>/", views.step_8, name="step_8"),
    path("survey/<str:pk>/<str:sk>/", views.survey, name="survey"),
    path("logbook_complete/<str:pk>/<str:sk>/", views.logbook_complete, name="logbook_complete"),
    path("notes/<str:pk>/<str:sk>/", views.notes, name="notes"),
    path(
        "preview_logbook/<str:pk>/<str:sk>/",
        views.preview_logbook,
        name="preview_logbook",
    ),
]
