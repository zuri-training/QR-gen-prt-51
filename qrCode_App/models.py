from django.db import models
from io import BytesIO
from django.utils import timezone
from django.core.files import File
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
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(self.qr_code_text)
        qr.make(fit=True)
        img = qr.make_image()
        img_io = BytesIO()
        img.save(img_io, format='PNG')
        file_name = '{0}_{1}.png'.format(self.user.full_name.split(" ")[0], self.qr_code_date)
        self.qr_code.save(file_name, File(img_io), save=False)
        super().save(*args, **kwargs)