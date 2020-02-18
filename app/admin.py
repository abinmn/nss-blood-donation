from django.contrib import admin


from app.models import District
from app.models import Taluk
from app.models import College
from app.models import BloodGroup
from app.models import Student
from app.models import VolunteerProfile
from app.models import Donation


admin.site.register(District)
admin.site.register(Taluk)
admin.site.register(College)
admin.site.register(BloodGroup)
admin.site.register(Student)
admin.site.register(VolunteerProfile)
admin.site.register(Donation)