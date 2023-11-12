from django.urls import path, include

from api.routers import router
from api.views import CreateLetter, RUDLetter, CreateLPackage, RUDPackager

urlpatterns = [
    # path("letter/create/", CreateLetter.as_view()),
    # path('letter/<int:pk>', RUDLetter.as_view()),
    #
    # path("package/create/", CreateLPackage.as_view()),
    # path('package/<int:pk>', RUDPackager.as_view()),
    path('', include(router.urls)),
]
