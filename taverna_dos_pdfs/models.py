from django.db import models
from django.utils import timezone
from django.conf import settings

from taverna_dos_pdfs.validator import validate_file_extension, validate_file_size


class PdfFile(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    pdf = models.FileField(upload_to='taverna_dos_pdfs/', validators=[validate_file_extension, validate_file_size])
    title = models.CharField(max_length=200)
    description = models.TextField()
    votes = models.IntegerField(default=0)
    created_at = models.DateTimeField(default=timezone.now)
    deleted_at = models.DateTimeField(default=None, null=True)

    def __str__(self):
        return self.title

