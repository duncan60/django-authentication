from django.db import models


class Draft(models.Model):
    PLATFORM = (
        ('ios', 'ios'),
        ('android', 'android')
    )
    platform = models.CharField(
        max_length=10,
        choices=PLATFORM,
        default='ios',
        verbose_name='裝置平台'
    )
    version = models.CharField(max_length=10, verbose_name='版本號')
    update_text = models.TextField(max_length=200, verbose_name='訊息文字')
    force_update = models.BooleanField(default=False, verbose_name='是否強更')
    pub_date = models.DateTimeField(verbose_name='發布日期')
    created_date = models.DateTimeField(
        auto_now_add=True,
        blank=True,
        verbose_name='建立日期')
    updated_date = models.DateTimeField(
        auto_now=True,
        blank=True,
        verbose_name='更新日期'
    )
    is_review = models.BooleanField(default=False, verbose_name='提交送審')

    def __str__(self):
        return f'{self.platform} - {self.version}'

    # def save(self, *args, **kwargs):
    #     if self.is_review:
    #         print(self)
    #         review = Review(draft=self)
    #         review.save()
    #     super().save(*args, **kwargs)

    class Meta:
        verbose_name = '草稿管理'
        # permissions = (('權限': '說名'), )
        unique_together = ('platform', 'version')


class UpdateInfo(models.Model):
    info = models.OneToOneField(
        Draft,
        verbose_name='發布訊息',
        null=True,
        blank=True,
        on_delete=models.SET_NULL)
    created_date = models.DateTimeField(
        auto_now_add=True,
        blank=True,
        verbose_name='建立日期')
    updated_date = models.DateTimeField(
        auto_now=True,
        blank=True,
        verbose_name='更新日期'
    )

    def __str__(self):
        return self.info.version

    class Meta:
        verbose_name = '版本發佈訊息'


class Review(models.Model):
    draft = models.ForeignKey(
        Draft,
        verbose_name='審核內容',
        on_delete=models.CASCADE)
    update_info = models.ForeignKey(
        UpdateInfo,
        null=True,
        blank=True,
        verbose_name='發佈更新',
        on_delete=models.SET_NULL)
    REVIEW_STATUS = (
        ('0', 'WAITING'),
        ('1', 'PASS'),
        ('2', 'NOT_PASS')
    )
    status = models.CharField(
        max_length=2,
        choices=REVIEW_STATUS,
        default='0',
        verbose_name='審核狀態'
    )
    created_date = models.DateTimeField(
        auto_now_add=True,
        blank=True,
        verbose_name='建立日期')
    updated_date = models.DateTimeField(
        auto_now=True,
        blank=True,
        verbose_name='更新日期'
    )

    def __str__(self):
        return f'{self.draft.platform} - {self.draft.version}'

    class Meta:
        verbose_name = '草稿審核'
