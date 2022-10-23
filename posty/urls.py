from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    path('create/', PostCreateView.as_view(), name="posty-create"),
    path('', PostListView.as_view(), name="posty-list"),
    path('<slug:slug>/', PostDetailView.as_view(), name="posty-detail"),
    path('<slug:slug>/update', PostUpdateView.as_view(), name="posty-update"),
    path('<slug:slug>/delete', PostDeleteView.as_view(), name="posty-delete"),
]
