from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt

from checkout.webhook_handler import StripeWH_Handler

import stripe
# webhooks.py contains a webhook function which takes a request
# code comes mostly from Stripe, just wh_secret instead of endpoint_secret
# and a generic exception handler

# the @require_POST means this view requires a POST request
# and won't accept a GET request
#


@require_POST
# Stripe won't send a csrf token so mark as exempt:
@csrf_exempt
def webhook(request):
    """Listen for webhooks from Stripe"""
    # Setup
    wh_secret = settings.STRIPE_WH_SECRET
    stripe.api_key = settings.STRIPE_SECRET_KEY

    # Get the webhook data and verify its signature
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
                payload, sig_header, wh_secret)
    except ValueError as e:
        # Invalid payload
        print('Error', e)
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        print('Error', e)
        return HttpResponse(status=400)
    except Exception as e:
        print('Error', e)
        return HttpResponse(content=e, status=400)
    # Set up a webhook handler
    handler = StripeWH_Handler(request)

    # Map webhook events to relevant handler functions
    event_map = {
        'payment_intent.succeeded': handler.handle_payment_intent_succeeded,
        'payment_intent.payment_failed': (handler.
                                          handle_payment_intent_payment_failed),
    }

    # Get the webhook type from Stripe
    event_type = event['type']

    # If there's a handler for it, get it from the event map
    # Use the generic one by default
    event_handler = event_map.get(event_type, handler.handle_event)

    # Call the event handler with the event
    response = event_handler(event)
    # Return the reponse to Stripe
    return response
