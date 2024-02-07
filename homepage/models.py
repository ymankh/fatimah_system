from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver


class HomePage(models.Model):
    title = models.CharField(max_length=500, help_text="The title that will apear on thehome page.")
    main_text = models.TextField(help_text="This will apear on the home page besid the title.")
    main_image = models.ImageField(help_text= "The image on teh homepage.",upload_to='homepage_images/')

    def __str__(self):
        return self.title

@receiver(pre_save, sender=HomePage)
def limit_homepage_instances(sender, instance, **kwargs):
    if HomePage.objects.exists() and not instance.pk:
        # Prevent creating more than one instance of HomePage
        raise ValueError("Only one instance of HomePage is allowed.")