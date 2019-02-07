from django.db import models

# Create your models here.


class Draft(models.Model):
    PLATFORM = (
        ('IOS', 'ios'),
        ('ANDROID', 'android')
    )
    platform = models.CharField(
        max_length=20,
        choices=PLATFORM,
        default='IOS',
        verbose_name='裝置平台'
    )
    version = models.CharField(
        max_length=10,
        verbose_name='版本號'
    )
    update_text = models.TextField(
        max_length=200,
        verbose_name='訊息文字'
    )
    force_update = models.BooleanField(
        default=False,
        verbose_name='是否強更'
    )
    pub_date = models.DateTimeField(
        verbose_name='發布日期'
    )
    created_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='建立日期'
    )
    update_date = models.DateTimeField(
        auto_now=True,
        verbose_name='更新日期'
    )

    def __str__(self):
        return self.version

    class Meta:
        verbose_name = '更新文字草稿'
        # permissions = (('權限': '說名'), )
        unique_together = ('platform', 'version')


class UpdateInfo(models.Model):
    platform = models.CharField(max_length=20)
    version = models.CharField(max_length=10)
    update_text = models.TextField(max_length=200)
    force_update = models.BooleanField(default=False)
    pub_date = models.DateTimeField('date published')
    is_pub = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.version


class Review(models.Model):
    is_review = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
