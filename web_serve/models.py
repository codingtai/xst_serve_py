from django.db import models


# Create your models here.
class PhotoList(models.Model):
    name = models.CharField(verbose_name='图片名', max_length=10, default="")
    photo = models.ImageField(verbose_name='图片资源', upload_to='photo_list')

    class Meta:
        db_table = 'photo_list'
        verbose_name_plural = '详情图片列表'

    def __str__(self):
        return '%s_%s' % (self.name, self.photo)


class DetailKind(models.Model):
    kind_name = models.CharField(verbose_name='分类名字', max_length=10)
    router = models.CharField(verbose_name='路由', max_length=10, default="")

    class Meta:
        db_table = 'detail_kind'
        verbose_name_plural = '详情分类'

    def __str__(self):
        return '%s_%s' % (self.kind_name, self.router)


# class RankList(models.Model):
#     name = models.CharField(verbose_name='排行榜', default="", max_length=10)
#
#     class Meta:
#         db_table = 'rank'
#         verbose_name_plural = '排行榜'
#
#     def __str__(self):
#         return '%s' % self.name


class PersonalData(models.Model):
    sex = models.CharField(verbose_name='性别', max_length=2)
    resume = models.CharField(verbose_name='个人简介', max_length=50)
    birthday = models.CharField(verbose_name='生日', max_length=32)

    class Meta:
        db_table = 'personal_data'
        verbose_name_plural = '个人资料'

    def __str__(self):
        return '%s_%s_%s' % (self.sex, self.resume, self.birthday)


class UserInfo(models.Model):
    username = models.CharField(verbose_name='用户名', max_length=32)
    mobile_phone = models.CharField(verbose_name='手机号', max_length=32)
    password = models.CharField(verbose_name='密码', max_length=32)
    header_img = models.ImageField(verbose_name='头像', upload_to='header_img')
    data_id = models.ForeignKey(PersonalData, on_delete=models.CASCADE, verbose_name='个人资料ID')

    class Meta:
        db_table = 'user'
        verbose_name_plural = '用户信息'

    def __str__(self):
        return '%s_%s_%s_%s' % (self.username, self.mobile_phone, self.password, self.header_img)


class Detail(models.Model):
    title = models.CharField(verbose_name='文章标题', max_length=32)
    content = models.TextField(verbose_name='文章内容')
    photo = models.ImageField(verbose_name='默认文章配图', upload_to='default_photo')
    photo_list = models.ForeignKey(PhotoList, on_delete=models.CASCADE, verbose_name='图片列表')
    kind_id = models.ForeignKey(DetailKind, on_delete=models.CASCADE, verbose_name='详情分类')
    user_id = models.ForeignKey(UserInfo, on_delete=models.CASCADE, verbose_name='用户id', default="")

    class Meta:
        db_table = 'detail'
        verbose_name_plural = '详情'

    def __str__(self):
        return '%s_%s_%s_%s' % (self.title, self.kind_id, self.user_id, self.photo)


class Comment(models.Model):
    content = models.TextField(verbose_name='根评论')
    datetime = models.CharField(verbose_name='评论时间', max_length=10)
    detail_id = models.OneToOneField(Detail, on_delete=models.CASCADE, verbose_name='详情ID')
    kind_id = models.OneToOneField(DetailKind, on_delete=models.CASCADE, verbose_name='种类ID')
    from_uid = models.OneToOneField(UserInfo, on_delete=models.CASCADE, verbose_name='评论用户ID')

    class Meta:
        db_table = 'comment'
        verbose_name_plural = '根评论'

    def __str__(self):
        return '%s_%s' % (self.content, self.datetime)


class HomeBanner(models.Model):
    name = models.CharField(verbose_name='图片名', max_length=10, default="")
    banner_photo = models.ImageField(upload_to='banner', verbose_name="轮播图")
    index = models.IntegerField(verbose_name='序号')
    detail_id = models.ForeignKey(Detail, on_delete=models.CASCADE, verbose_name='详情ID')

    class Meta:
        db_table = 'home_banner'
        verbose_name_plural = '首页轮播图'

    def __str__(self):
        return '%s_%s_%s' % (self.name, self.banner_photo, self.index)


class HomeKindShow(models.Model):
    detail_id = models.ForeignKey(Detail, on_delete=models.CASCADE, verbose_name='详情ID')
    kind_id = models.ForeignKey(DetailKind, on_delete=models.CASCADE, verbose_name='分类ID')

    class Meta:
        db_table = 'home_kind_show'
        verbose_name_plural = '首页分类展示'

    def __str__(self):
        return '%s_%s' % (self.detail_id, self.kind_id)


class Reply(models.Model):
    reply_type = models.CharField(verbose_name='评论类型 comment或reply', max_length=10)
    content = models.TextField(verbose_name='回复评论')
    datetime = models.CharField(verbose_name='回复时间', max_length=10)
    comment_id = models.OneToOneField(Comment, on_delete=models.CASCADE, verbose_name='根评论ID')
    from_uid = models.OneToOneField(UserInfo, on_delete=models.CASCADE, related_name='from_uid', verbose_name='发布评论用户ID')
    to_uid = models.OneToOneField(UserInfo, on_delete=models.CASCADE, related_name='to_uid', verbose_name='回复用户ID')

    class Meta:
        db_table = 'reply'
        verbose_name_plural = '回复评论'

    def __str__(self):
        return '%s_%s_%s' % (self.reply_type, self.content, self.datetime)


class Solution(models.Model):
    content = models.TextField(verbose_name='解决方案')
    datetime = models.CharField(verbose_name='解决时间', max_length=10)
    detail_id = models.OneToOneField(Detail, on_delete=models.CASCADE, verbose_name='详情ID')
    from_uid = models.OneToOneField(UserInfo, on_delete=models.CASCADE, verbose_name='相关部门用户')

    class Meta:
        db_table = 'solution'
        verbose_name_plural = '解决方案'

    def __str__(self):
        return '%s_%s' % (self.content, self.datetime)


