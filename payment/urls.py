from django.urls import path

urlpatterns = [
    path("<int:course_id>/",pass,name="create_checkout_session"),
    path("course_success/<int:course_id>",pass, name="course_success"),
    path("course_cancel",pass,name="course_cancel"),
    path("stripe/webhook",pass,name="stripe_webhook")


]
