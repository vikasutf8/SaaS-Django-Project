from django.shortcuts import render, redirect,get_object_or_404,reverse
import stripe 
from course.models import Course
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

from django.views.decorators.http import require_POST
from django.utils.encoding import smart_str
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


   
stripe.api_key =settings.STRIPE_SECRET_KET

# Create your views here.
@login_required
def create_chechout_session(request,course_id):
    course =get_object_or_404(Course,pk=course_id)

    price_in_cents=int(course.price*100)

    session =stripe.checkout.Session.create(
         payment_method_types=["card"],
         line_items=[{
              "price_data":{
                   "currency":"usd",
                   "unit_amount": price_in_cents
                   "product_data":{
                        "name":course.title 
                   },
                },
              "quantity":1
         }],
         mode="payment",
         success_url =request.build_absolute_uri(reverse("course_success"))
         cancel_url =request.build_absolute_uri(reverse("course_cancel"))
         matadata =("course_id":course_id,"user_id":request.user.id)
    )
    return redirect(session.url)

@csrf_exempt
@require_POST
def stripe_webhook(request):
    return None

def handle_checkout_session(session):
    return None

@login_required
def course_success(request):
        return redirect("course_list")

@login_required
def course_cancel(request):
     return