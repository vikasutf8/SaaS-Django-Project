from django.urls import path
from.import views


urlpatterns = [
    path("<int:course_id>/",views.create_chechout_session,pass,name="create_checkout_session"),
    path("course_success/",views.course_success,pass, name="course_success"),
    path("course_cancel",views.course_cancel,pass,name="course_cancel"),
    path("stripe/webhook",views.stripe_webhook,pass,name="stripe_webhook")


]
