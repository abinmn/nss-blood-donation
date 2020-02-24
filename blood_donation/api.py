from rest_framework import routers
from app.views import district
from app.views import blood_group
from app.views import college
from app.views import student


router = routers.DefaultRouter()
router.register('districts', district.DistrictViewset)
router.register('blood-groups', blood_group.BloodGroupViewset)
router.register('search-availability', college.CollegeByTalukViewset, basename='filter-by-college')
router.register('colleges', college.CollegeDetailsViewset)
router.register('students', student.StudentViewset, basename='students')