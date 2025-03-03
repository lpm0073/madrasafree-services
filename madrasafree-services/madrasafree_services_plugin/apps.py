"""
madrasafree_services Django application initialization.
"""
# Check this for an example of using edx django plugin
# https://github.com/openedx/edx-bulk-grades/blob/master/bulk_grades/apps.py
from django.apps import AppConfig


class MadrasafreeServicesConfigPlugin(AppConfig):
#Configuration for the madrasafree_services Django application.


    name = 'madrasafree_services_plugin'
    label = 'mad'
    plugin_app = {
        'url_config': {
             'lms.djangoapp': {
                 'namespace': 'madrasa_service_plugin',
                 'regex': '^madrasa_api/',
                 'relative_path': 'urls',
             },
        },
        'settings_config': {
            'lms.djangoapp': {
                'production': { 'relative_path': 'settings.production' },
                'common': { 'relative_path': 'settings.common' },
            }
        },

    }
