# Generated by Django 3.2.16 on 2023-02-09 03:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name='根评论')),
                ('datetime', models.CharField(max_length=10, verbose_name='评论时间')),
            ],
            options={
                'verbose_name_plural': '根评论',
                'db_table': 'comment',
            },
        ),
        migrations.CreateModel(
            name='Detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, verbose_name='文章标题')),
                ('content', models.TextField(verbose_name='文章内容')),
                ('photo', models.ImageField(upload_to='default_photo', verbose_name='默认文章配图')),
            ],
            options={
                'verbose_name_plural': '详情',
                'db_table': 'detail',
            },
        ),
        migrations.CreateModel(
            name='DetailKind',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kind_name', models.CharField(max_length=10, verbose_name='分类名字')),
                ('router', models.CharField(default='', max_length=10, verbose_name='路由')),
            ],
            options={
                'verbose_name_plural': '详情分类',
                'db_table': 'detail_kind',
            },
        ),
        migrations.CreateModel(
            name='PersonalData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sex', models.CharField(max_length=2, verbose_name='性别')),
                ('resume', models.CharField(max_length=50, verbose_name='个人简介')),
                ('birthday', models.CharField(max_length=32, verbose_name='生日')),
            ],
            options={
                'verbose_name_plural': '个人资料',
                'db_table': 'personal_data',
            },
        ),
        migrations.CreateModel(
            name='PhotoList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=10, verbose_name='图片名')),
                ('photo', models.ImageField(upload_to='photo_list', verbose_name='图片资源')),
            ],
            options={
                'verbose_name_plural': '详情图片列表',
                'db_table': 'photo_list',
            },
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=32, verbose_name='用户名')),
                ('mobile_phone', models.CharField(max_length=32, verbose_name='手机号')),
                ('password', models.CharField(max_length=32, verbose_name='密码')),
                ('header_img', models.ImageField(upload_to='header_img', verbose_name='头像')),
                ('data_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web_serve.personaldata', verbose_name='个人资料ID')),
            ],
            options={
                'verbose_name_plural': '用户信息',
                'db_table': 'user',
            },
        ),
        migrations.CreateModel(
            name='Solution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name='解决方案')),
                ('datetime', models.CharField(max_length=10, verbose_name='解决时间')),
                ('detail_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='web_serve.detail', verbose_name='详情ID')),
                ('from_uid', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='web_serve.userinfo', verbose_name='相关部门用户')),
            ],
            options={
                'verbose_name_plural': '解决方案',
                'db_table': 'solution',
            },
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reply_type', models.CharField(max_length=10, verbose_name='评论类型 comment或reply')),
                ('content', models.TextField(verbose_name='回复评论')),
                ('datetime', models.CharField(max_length=10, verbose_name='回复时间')),
                ('comment_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='web_serve.comment', verbose_name='根评论ID')),
                ('from_uid', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='from_uid', to='web_serve.userinfo', verbose_name='发布评论用户ID')),
                ('to_uid', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='to_uid', to='web_serve.userinfo', verbose_name='回复用户ID')),
            ],
            options={
                'verbose_name_plural': '回复评论',
                'db_table': 'reply',
            },
        ),
        migrations.CreateModel(
            name='HomeKindShow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detail_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web_serve.detail', verbose_name='详情ID')),
                ('kind_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web_serve.detailkind', verbose_name='分类ID')),
            ],
            options={
                'verbose_name_plural': '首页分类展示',
                'db_table': 'home_kind_show',
            },
        ),
        migrations.CreateModel(
            name='HomeBanner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=10, verbose_name='图片名')),
                ('banner_photo', models.ImageField(upload_to='banner', verbose_name='轮播图')),
                ('index', models.IntegerField(verbose_name='序号')),
                ('detail_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web_serve.detail', verbose_name='详情ID')),
            ],
            options={
                'verbose_name_plural': '首页轮播图',
                'db_table': 'home_banner',
            },
        ),
        migrations.AddField(
            model_name='detail',
            name='kind_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web_serve.detailkind', verbose_name='详情分类'),
        ),
        migrations.AddField(
            model_name='detail',
            name='photo_list',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web_serve.photolist', verbose_name='图片列表'),
        ),
        migrations.AddField(
            model_name='detail',
            name='user_id',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='web_serve.userinfo', verbose_name='用户id'),
        ),
        migrations.AddField(
            model_name='comment',
            name='detail_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='web_serve.detail', verbose_name='详情ID'),
        ),
        migrations.AddField(
            model_name='comment',
            name='from_uid',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='web_serve.userinfo', verbose_name='评论用户ID'),
        ),
        migrations.AddField(
            model_name='comment',
            name='kind_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='web_serve.detailkind', verbose_name='种类ID'),
        ),
    ]