import random
from django import forms
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from django.conf import settings
from utils.tencent.sms import send_sms_single
from django_redis import get_redis_connection


class RegisterForm(forms.Form):
    mobile_phone = forms.CharField(label='手机号', validators=[RegexValidator(r'^(1[3|4|5|6|7|8|9])\d{9}$', '手机号格式错误'), ])
    code = forms.CharField(label='验证码')

    def clean_mobile_phone(self):
        mobile_phone = self.cleaned_data['mobile_phone']
        return mobile_phone

    def clean_code(self):

        code = self.cleaned_data['code']
        mobile_phone = self.cleaned_data['mobile_phone']

        conn = get_redis_connection()
        redis_code = conn.get(mobile_phone)
        if not redis_code:
            raise ValidationError('验证码失效或未发送，请重新发送')

        redis_str_code = redis_code.decode('utf-8')

        if code.strip() != redis_str_code.strip():
            raise ValidationError('验证码错误，请重新输入')

        return code


class SendSmsForm(forms.Form):
    mobile_phone = forms.CharField(label='手机号', validators=[RegexValidator(r'^(1[3|4|5|6|7|8|9])\d{9}$', '手机号格式错误'), ])

    def __init__(self, request, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.request = request

    def clean_mobile_phone(self):
        # 手机号验证钩子
        mobile_phone = self.cleaned_data['mobile_phone']
        # 判断短信模板是否有问题
        tpl = self.request.GET.get('tpl')
        template_id = settings.TENCENT_SMS_TEMPLATE.get(tpl)
        if not template_id:
            raise ValidationError('短信模板错误')

        # 发短信
        code = random.randrange(1000, 9999)

        sms = send_sms_single(mobile_phone, template_id, [code, ])
        if sms['result'] != 0:
            raise ValidationError("短信发送失败, {}".format(sms['errmsg']))

        # 验证码写入redis
        conn = get_redis_connection()
        conn.set(mobile_phone, code, ex=60)

        return mobile_phone


class LoginForm(forms.Form):
    phonenum = forms.CharField(label='手机号', validators=[RegexValidator(r'^(1[3|4|5|6|7|8|9])\d{9}$', '手机号格式错误'), ])
    password = forms.CharField(label='密码', max_length=12, min_length=6)

