# 引入Django表单
from  django import forms
from UserManage.models import User


# 重置密码form实现
class UpdatePwdForm(forms.Form):
    # 密码不能小于5位
    password1 = forms.CharField(required=True, min_length=5)
    # 密码不能小于5位
    password2 = forms.CharField(required=True, min_length=5)


# 用于个人中心修改个人信息
class UserInfoForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['nickname','gender','address','mobile', 'email']