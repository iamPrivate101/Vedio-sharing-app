from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.validators import FileExtensionValidator


class Video(models.Model):
    uploader = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    video_file = models.FileField(
        upload_to="uploads/video_files",
        validators=[FileExtensionValidator(allowed_extensions=["mp4"])],
    )  # mp4 extension is only allowed in vedi
    thumbnail = models.FileField(
        upload_to="uploads/thumbnails",
        validators=[FileExtensionValidator(allowed_extensions=["png", "jpg", "jpeg"])],
    )  # png, jpg , jpeg are only supported by thumbnails
    date_posted = models.DateTimeField(default=timezone.now)
