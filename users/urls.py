from rest_framework.routers import DefaultRouter

from users.apps import UsersConfig
from users.views import UserViewSet

app_name = UsersConfig.name

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='пользователи')

url_patterns = [

]