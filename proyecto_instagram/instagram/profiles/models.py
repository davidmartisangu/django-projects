from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE,related_name='profile')
    profile_picture=models.ImageField('Imagen de perfil', upload_to='profile_pictures/', blank=True, null=True)
    bio=models.TextField('Biografia', max_length=500, blank=True)
    birth_date=models.DateField('Fecha de nacimiento', null=True, blank=True)
    followers=models.ManyToManyField("self", symmetrical=False, related_name="following", through="Follow")

    class Meta:
        verbose_name='Perfil'
        verbose_name_plural='Perfiles'

    def __str__(self):
        return self.user.username
    
    def follow(self, profile):
        Follow.objects.get_or_create(follower=self, following=profile)

    def unfollow(self, profile):
        if Follow.objects.filter(follower=self, following=profile).count():
            Follow.objects.filter(follower=self, following=profile).delete()
            return True
        return False

    def like_post(self, post):
        post.like(self.user)

    def unlike_post(self,post):
        post.unlike(self.user)
    
class Follow(models.Model):
    follower=models.ForeignKey(UserProfile, verbose_name="¿Quien sigue?", on_delete=models.CASCADE, related_name="follower_set")
    # ForeignKey => Relación muchos a uno (muchos perfiles pueden seguir a un perfil, y un perfil puede seguir a muchos otros).
    following=models.ForeignKey(UserProfile, verbose_name="¿A quien sigue?", on_delete=models.CASCADE, related_name="following_set")
    created_at=models.DateTimeField(auto_now_add=True, verbose_name="¿Desde cuando lo sigue?")

    class Meta:
        unique_together = ("follower", "following")
        # unique_together garantiza que la combinación de los campos follower y following sea única, evitando que un usuario siga al mismo perfil más de una vez.
        verbose_name='Seguidor'
        verbose_name_plural='Seguidores'

    def __str__(self):
        return f"{self.follower} follows{self.following}"
