from rest_framework import routers
from app.views import district


router = routers.DefaultRouter()
router.register('districts', district.DistrictViewset)