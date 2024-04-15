from django.urls import path

from . import views

urlpatterns = [
    # ex: /disks/
    path("", views.index, name="index"),
    # ex: /disks/5/
    path("<str:title>/", views.album, name="album"),
    # # ex: /disks/5/results/
    # path("<int:question_id>/results/", views.results, name="results"),
    # # ex: /polls/5/vote/
    # path("<int:question_id>/vote/", views.vote, name="vote"),
]