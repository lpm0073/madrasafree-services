"""
URLs for madrasafree_services.
"""
from django.urls import re_path  # pylint: disable=unused-import
from django.views.generic import TemplateView  # pylint: disable=unused-import

from .views import icredit_get_url, payment_success
#registration_completed, icredit_payment_success, donate, donate_success

urlpatterns = [
    re_path(r'icredit_get_url', icredit_get_url, name='icredit_get_url'),
    re_path(r'payment_success', payment_success)
]
