"""
madrasafree_services Django application initialization.
"""
# Check this for an example of using edx django plugin
# https://github.com/openedx/edx-bulk-grades/blob/master/bulk_grades/apps.py
from django.apps import AppConfig
from django.conf import settings
from edx_django_utils.plugins import PluginSettings, PluginURLs
from openedx.core.djangoapps.plugins.constants import ProjectType, SettingsType


class MadrasafreeServicesConfigPlugin(AppConfig):
    # Configuration for the madrasafree_services Django application.

    name = 'madrasafree_services_plugin'
    label = 'mad'

    # See: https://edx.readthedocs.io/projects/edx-django-utils/en/latest/edx_django_utils.plugins.html
    plugin_app = {
        PluginURLs.CONFIG: {
            ProjectType.LMS: {
                PluginURLs.NAMESPACE: name,
                PluginURLs.REGEX: "^madrasa_api",
                PluginURLs.RELATIVE_PATH: "urls",
            }
        },
        PluginSettings.CONFIG: {
            ProjectType.LMS: {
                # uncomment these to activate
                SettingsType.PRODUCTION: {PluginSettings.RELATIVE_PATH: "settings.production"},
                SettingsType.COMMON: {PluginSettings.RELATIVE_PATH: "settings.common"},
            }
        },

    }
