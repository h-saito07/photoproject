from django.db import models
# AbstracUserクラスをインポート
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    '''
    Userモデルを継承したカスタムユーザモデル
    '''
    pass