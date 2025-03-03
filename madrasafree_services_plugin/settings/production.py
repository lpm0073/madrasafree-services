from pathlib import Path
DEBUG = True
#ROOT_URLCONF="madrasafree_services.urls"
#DIRS.append("madrasafree-services/madrasafree_services")
SECRET_KEY="sergsegr343"
ICREDIT_API_URL = "https://testicredit.rivhit.co.il/API/PaymentPageRequest.svc/GetUrl"
ICREDIT_GROUP_PRIVATE_TOKEN = "6ff3d7c6-001c-48ea-a6c8-9482791c1d60"
REDIRECT_URL = "http://localhost:8000/payment_success"
#BASE_DIR = Path(__file__).resolve().parent.parent
#print(BASE_DIR)
"""
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
        'DIRS':[BASE_DIR/'madrasafree_services_plugin/templates/madrasafree_services'],
        'OPTIONS': {
            'context_processors': [
                "django.contrib.auth.context_processors.auth",
            ]
        }

    },
]
"""
def plugin_settings(settings):
    settings.ICREDIT_API_URL="https://icredit.rivhit.co.il/API/PaymentPageRequest.svc/GetUrl"
    settings.ICREDIT_GROUP_PRIVATE_TOKEN="0be5fb5b-e7d2-45d7-956e-7f1af1f61097"
    settings.REDIRECT_URL = "https://courses.madrasafree.com/madrasa_api/payment_success"
#    settings.TEMPLATES.append(TEMPLATES[0])
    # Update the provided settings module with any app-specific settings.
    # For example:
    #     settings.FEATURES['ENABLE_MY_APP'] = True
    #     settings.MY_APP_POLICY = 'foo'
