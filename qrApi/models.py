from io import BytesIO
from django.db import models
import qrcode
from django.core.files import File
from PIL import Image, ImageDraw

# Create your models here.


Color = (
    ("WHITE", "white"),
    ("BLUE", "blue"),
    ("RED", "red"),
    ("YELLOW", "yellow"),
    ("BLACK", "black"),
)


class QrcodeApi(models.Model):
    title = models.CharField(max_length=50, blank=True, null=True)
    date = models.DateField(("date"), auto_now=True, auto_now_add=False)
    qr_code = models.ImageField(upload_to="qr_codesApi", blank=True)
    bg_color = models.CharField(max_length=50, choices=Color, null=True)
    qr_color = models.CharField(max_length=50, choices=Color, null=True)

    def save(self, *args, **kwargs):
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(self.title)
        qr.make(fit=True)
        qr_code = qr.make_image(
            fill_color=f"{self.qr_color}", back_color=f"{self.bg_color}"
        )
        fname = f"Qr_Code-{self.title}.png"
        buffer = BytesIO()
        qr_code.save(buffer, "PNG")
        self.qr_code.save(fname, File(buffer), save=False)
        super().save(*args, **kwargs)


class TestModel(models.Model):

    title = models.CharField(max_length=50, blank=True, null=True)
    qr_code = models.ImageField(upload_to="qr_codesApi", blank=True)
    date = models.DateField(("date"), auto_now=False, auto_now_add=True)

    def save(self, *args, **kwargs):
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(self.title)
        qr.make(fit=True)
        qr_code = qr.make_image(fill_color="black", back_color="white")
        fname = f"Qr_Code-{self.title}.png"
        buffer = BytesIO()
        qr_code.save(buffer, "PNG")
        self.qr_code.save(fname, File(buffer), save=False)
        super().save(*args, **kwargs)
