from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True) # 자동으로 입력 시간
    updated_at = models.DateTimeField(auto_now = True)
    head_image = models.ImageField(upload_to = 'blog/images/%Y/%m/%d/', blank=True)
    file_upload = models.FileField(upload_to = 'blog/files/%Y/%m/%d', blank=True)


    def __str__(self):
        return f'[{self.pk}]{self.title}'   #pk: 각 레코드에 대한 고유의 값./ title: 제목


    def get_absolute_url(self):
        return f'/blog/{self.pk}/'




