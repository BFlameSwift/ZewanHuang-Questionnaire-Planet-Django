from django.conf.urls.static import static
from django.urls import path
from .views import *


urlpatterns = [

    path('delete/qn/not_real/',delete_survey_not_real),
    path('delete/qn/real/',delete_survey_real),
    path('delete/question/',delete_question),
    path('delete/option/',delete_option),

    path('get/qn_detail/',get_survey_details),

]
