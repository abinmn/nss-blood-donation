from rest_framework import routers
from app.views import district
from app.views import blood_group


router = routers.DefaultRouter()
router.register('districts', district.DistrictViewset)
router.register('blood-groups', blood_group.BloodGroupViewset)