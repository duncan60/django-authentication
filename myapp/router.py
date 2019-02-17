from versionInfo.api.viewsets import UpdateInfoViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register('versionInfo', UpdateInfoViewSet, base_name='versionInfo')

# for url in router.urls:
#     print(url, '\n')
