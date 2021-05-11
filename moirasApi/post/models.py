from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.utils import timezone

class Post(models.Model):
    aboutData = models.CharField(verbose_name='About',max_length=100)
    title = models.CharField(verbose_name='Называние',max_length=200)
    content = RichTextField(blank=True,null=True)
    rat_indicator = models.BigIntegerField(verbose_name='Рейтинг',default=0)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    created_at = models.DateTimeField(("Дата создание"),auto_now_add=timezone.now())
    urlContent = models.URLField(verbose_name='UrlКонтент',max_length=500,null=True,blank=True)
    

    def __str__(self):
        return f'Task: {self.title}'
    
    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'


class ImagePost(models.Model):
    aboutData = models.CharField(verbose_name='About',max_length=100)
    title = models.CharField(verbose_name='Называние',max_length=200)
    rat_indicator = models.BigIntegerField(verbose_name='Рейтинг',default=0)
    image = models.ImageField(verbose_name='Post Image')
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    created_at = models.DateTimeField(("Дата создание"),auto_now_add=timezone.now())

    def __str__(self):
        return f'Task: {self.title}'
    
    class Meta:
        verbose_name = 'ImagePost'
        verbose_name_plural = 'ImagePosts'


class UrlPost(models.Model):
    aboutData = models.CharField(verbose_name='About',max_length=100)
    title = models.CharField(verbose_name='Называние',max_length=200)
    urlContent = models.URLField(verbose_name='UrlКонтент',max_length=500)
    rat_indicator = models.BigIntegerField(verbose_name='Рейтинг',default=0)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    created_at = models.DateTimeField(("Дата создание"),auto_now_add=timezone.now())
    titileImage = models.ImageField(verbose_name='Post Image',null=True,blank=True)

    def __str__(self):
        return f'Task: {self.title}'
        
    class Meta:
        verbose_name = 'UrlPost'
        verbose_name_plural = 'UrlPosts'

class Comment(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    comment = RichTextField()
    rat_indicator = models.BigIntegerField(verbose_name='Рейтинг',default=0)
    created_at = models.DateTimeField(("Дата создание"),auto_now_add=timezone.now())

    post = models.ForeignKey(Post,on_delete=models.CASCADE,null=True,default=None,blank=True)
    imagepost = models.ForeignKey(ImagePost,on_delete=models.CASCADE,null=True,default=None,blank=True)
    urlpost = models.ForeignKey(UrlPost,on_delete=models.CASCADE,null=True,default=None,blank=True)


    def __str__(self):
        return f'Task: {self.created_at}'
        
    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'