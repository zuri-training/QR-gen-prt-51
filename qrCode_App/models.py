from tkinter import Canvas
from django.db import models
from io import BytesIO
from django.utils import timezone
from django.core.files import File
from PIL import Image, ImageDraw
import qrcode

def get_upload_path(instance, filename):
    return 'for_{0}_{1}/{2}'.format(instance.user.full_name.split(" ")[0], instance.user.id, filename)

# Create your models here.

class QrCode(models.Model):
    user = models.ForeignKey('accounts.CustomUser', null=True, on_delete=models.CASCADE)
    qr_type = models.CharField(max_length=100)
    qr_code_text = models.TextField()
    qr_msg = models.TextField(null=True)
    qr_code = models.ImageField(upload_to=get_upload_path, blank=True, null=True)
    qr_code_date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.user.full_name

    def save(self, *args, **kwargs):
        code_image = qrcode.make(self.qr_code_text)
        canvas = Image.new('RGB', (800,800), 'white')
        draw = ImageDraw.Draw(canvas)
        canvas.paste(code_image)
        file_name = '{0}_{1}.png'.format(self.user.full_name.split(" ")[0], self.qr_code_date)
        output = BytesIO()
        canvas.save(output, format='PNG')
        self.qr_code.save(file_name, File(output), save=False)
        super().save(*args, **kwargs)
