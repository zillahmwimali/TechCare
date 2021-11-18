from django.contrib import admin
from chw.models import Referral,MotherAssessment,GeneralAssessment,ChildAssessment
from core.models import Chw,User


admin.site.register(User)
admin.site.register(Chw)
admin.site.register(Referral)
admin.site.register(GeneralAssessment)
admin.site.register(MotherAssessment)
admin.site.register(ChildAssessment)












