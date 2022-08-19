from django.shortcuts import render, reverse
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from .models import Video
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

"""
LoginRequiredMixin --> checks if the user is loged in or not

UserPassesTestMixin --> returns true if the user has created the video and gives access other wise false , checks the user that has created video or not

"""


class Index(ListView):
    model = Video
    template_name = "videos/index.html"
    order_by = '-date_posted'


class CreateVideo(LoginRequiredMixin, CreateView):
    model = Video
    # fields = "__all__"
    fields = ["title", "description", "video_file", "thumbnail"]
    template_name = "videos/create_video.html"

    #setting user on the form
    def form_valid(self,form):
        form.instance.uploader = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("video-detail", kwargs={"pk": self.object.pk})


class DetailVideo(DetailView):
    model = Video
    template_name = "videos/detail_video.html"


class UpdateVideo(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Video
    fields = ["title", "description"]
    template_name = "videos/create_video.html"

    def get_success_url(self):
        return reverse("video-detail", kwargs={"pk": self.object.pk})
#checking the user has created the video or not , if viedo is created by the same user  access is given by UserPassesTestMixin 
    def test_func(self):
        video = self.get_object()
        return self.request.user == video.uploader

class DeleteVideo(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Video
    template_name = 'videos/delete_video.html'

    def get_success_url(self) :
        return reverse('index')
#checking the user has created the video or not , if viedo is created by the same user  access is given by UserPassesTestMixin 
    def test_func(self):
        video = self.get_object()
        return self.request.user == video.uploader
