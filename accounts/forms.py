from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    '''UserCreateonFormのサブクラス
    '''
    class Meta:
        '''UserCreationFormのインナークラス

        Attributes:
            model:連携するUserモデル
            fields:フォームで使用するフィールド
        '''
        # 連携するUserモデルを設定
        model = CustomUser
        # フォームで使用するフィールドを設定
        # ユーザー名、メールアドレス、パスワード、パスワード(確認用)
        fields = ('username', 'email', 'password1', 'password2')