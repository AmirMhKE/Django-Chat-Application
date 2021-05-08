from django.db import models
from django.contrib.auth import get_user_model

user = get_user_model()

class Chat(models.Model):
    room_name = models.CharField(blank=True, max_length=50, verbose_name="نام اتاق")
    members = models.ManyToManyField(user, blank=True, verbose_name="ممبرها")

    def __str__(self):
        return self.room_name

    class Meta:
        verbose_name = "چت"
        verbose_name_plural = "چت ها"

class Message(models.Model):
    author = models.ForeignKey(user, on_delete=models.CASCADE, verbose_name="نویسنده")
    content = models.TextField(verbose_name="محتوا")
    related_chat = models.ForeignKey(Chat, on_delete=models.CASCADE, blank=True, verbose_name="گروه مقصد")
    timestamp = models.DateTimeField(auto_now_add=True)

    def last_message(self, room_name):
        return Message.objects.order_by("-timestamp").filter(related_chat__room_name=room_name)

    def __str__(self):
        return f"{self.author.username}"

    class Meta:
        verbose_name = "پیام"
        verbose_name_plural = "پیام ها"    