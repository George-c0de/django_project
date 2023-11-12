from rest_framework import routers

from api.views import LetterViewSet, PackageViewSet

router = routers.DefaultRouter()
router.register(r'letters', LetterViewSet)
router.register(r'package', PackageViewSet)
