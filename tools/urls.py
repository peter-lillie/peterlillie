"""
URL configuration for peterlillie project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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

from . import views as tools_views
from django.urls import path

urlpatterns = [
    # path("", view=tools_views.all_tools, name="all_tools"),
    path("todo/", view=tools_views.todo_main, name="todo"),
    path('submit-todo', tools_views.submit_todo, name='submit-todo'),
    path('complete-todo/<int:pk>/', tools_views.complete_todo, name='complete-todo'),
    path('delete-todo/<int:pk>/', tools_views.delete_todo, name='delete-todo'),
    ]
