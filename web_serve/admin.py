from django.contrib import admin
from web_serve.models import PhotoList, DetailKind, Detail, PersonalData, UserInfo, Comment, \
    HomeBanner, HomeKindShow, Reply, Solution


# Register your models here.
class PhotoListManager(admin.ModelAdmin):
    list_display = ['id', 'name', 'photo']


class DetailKindManager(admin.ModelAdmin):
    list_display = ['id', 'kind_name', 'router']


class DetailManager(admin.ModelAdmin):
    list_display = ['id', 'kind_id', 'title', 'photo', 'user_id']


class PersonalDataManager(admin.ModelAdmin):
    list_display = ['id', 'sex', 'resume', 'birthday']


class UserManager(admin.ModelAdmin):
    list_display = ['id', 'username', 'mobile_phone', 'password', 'header_img']


class CommentManager(admin.ModelAdmin):
    list_display = ['id', 'content', 'datetime']


class HomeBannerManager(admin.ModelAdmin):
    list_display = ['id', 'name', 'banner_photo', 'index']


class HomeKindShowManager(admin.ModelAdmin):
    list_display = ['id', 'kind_id', 'detail_id']


class ReplyManager(admin.ModelAdmin):
    list_display = ['id', 'reply_type', 'content', 'datetime']


class SolutionManager(admin.ModelAdmin):
    list_display = ['id', 'content', 'datetime']


admin.site.register(PhotoList, PhotoListManager)
admin.site.register(DetailKind, DetailKindManager)
admin.site.register(Detail, DetailManager)
admin.site.register(PersonalData, PersonalDataManager)
admin.site.register(UserInfo, UserManager)
admin.site.register(Comment, CommentManager)
admin.site.register(HomeBanner, HomeBannerManager)
admin.site.register(HomeKindShow, HomeKindShowManager)
admin.site.register(Reply, ReplyManager)
admin.site.register(Solution, SolutionManager)


