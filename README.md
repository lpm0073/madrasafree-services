# madrasafree-services

## Intro
This app does wrap all the functions that madrasa-free require for running Open edX platform in Django App, that is expected to be installed in the LMS. 

The repo was generated using cookiecutter from https://github.com/openedx/edx-cookiecutters using `cookiecutter-django-app` template. 

Part of the code here is incorporated from https://github.com/madrasafree/edx-platform/tree/e9aeda3b0ccefdfbbad69dd8b96eb0713b6afa89/madrasafree 


## Installation/Usage
Inside the lms/cms container run `pip install https://github.com/madrasafree/madrasafree-services`

In order to use iframe this setting need to be handeled in away or another: 

`MIDDLEWARE.remove('django.middleware.clickjacking.XFrameOptionsMiddleware')`

It can be appendned at `env/apps/openedx/settings/lms/production.py` 

Or using the plugin
```yaml
name: madarasa_plugin
version: 0.1.0
patches:
  lms-env: |
    "ADDL_INSTALLED_APPS": ["madrasafree_services"],
    "ENABLE_COMBINED_LOGIN_REGISTRATION": true,
    "REGISTRATION_EXTENSION_FORM": "madrasafree_services.forms.ExtraInfoForm"
    "THIRD_PARTY_AUTH_BACKENDS": ["social_core.backends.google.GoogleOAuth2"]
  cms-env: |
    "ENABLE_COMBINED_LOGIN_REGISTRATION": true
  openedx-lms-production-settings: |
    MIDDLEWARE.append('madrasafree_services.middleware.MadrasafreeMiddleware')
  openedx-auth: |
    "SOCIAL_AUTH_OAUTH_SECRETS": {"google-oauth2": "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"}
  common-env-features: |
    "ENABLE_THIRD_PARTY_AUTH": true
  openedx-common-settings: |
    FEATURES["CUSTOM_COURSES_EDX"] = True

REGISTRATION_EXTRA_FIELDS = {
    'confirm_email': 'hidden',
    'level_of_education': 'optional',
    'gender': 'optional',
    'year_of_birth': 'optional',
    'mailing_address': 'optional',
    'goals': 'optional',
    'honor_code': 'required',
    'terms_of_service': 'hidden',
    'city': 'hidden',
    'country': 'hidden',
    'first_name': 'required',
    'last_name': 'required'

}

```
```Caddyfile
:8002 {
    @mfe_donate {
        path /donate /donate/*
    }
    handle @mfe_donate {
        uri strip_prefix /donate
        root * /openedx/dist/donate
        try_files /{path} /index.html
        file_server
    }
}
```

## References
- https://github.com/openedx/edx-cookiecutters
- https://github.com/openedx/edx-django-utils 
- https://github.com/madrasafree/madrasa-theme/tree/master/lms/templates/madrasafree 

```
lms_1                        | all user propos ['DoesNotExist', 'EMAIL_FIELD', 'Meta', 'MultipleObjectsReturned', 'REQUIRED_FIELDS', 'USERNAME_FIELD', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setstate__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_check_column_name_clashes', '_check_constraints', '_check_default_pk', '_check_field_name_clashes', '_check_fields', '_check_id_field', '_check_index_together', '_check_indexes', '_check_local_fields', '_check_long_column_names', '_check_m2m_through_same_relationship', '_check_managers', '_check_model', '_check_model_name_db_lookup_clashes', '_check_ordering', '_check_property_name_related_field_accessor_clashes', '_check_single_primary_key', '_check_swappable', '_check_unique_together', '_do_insert', '_do_update', '_get_FIELD_display', '_get_expr_references', '_get_next_or_previous_by_FIELD', '_get_next_or_previous_in_order', '_get_pk_val', '_get_unique_checks', '_legacy_get_session_auth_hash', '_meta', '_password', '_perform_date_checks', '_perform_unique_checks', '_prepare_related_fields_for_save', '_save_parents', '_save_table', '_set_pk_val', '_state', 'account_recovery', 'accountrecoveryconfiguration_set', 'actor', 'anonymoususerid_set', 'api_access_request', 'apiaccessconfig_set', 'articlerevision_set', 'assetbaseurlconfig_set', 'assetexcludedextensionsconfig_set', 'attributes', 'backend', 'badgeassertion_set', 'blockcompletion_set', 'blockstructureconfiguration_set', 'bookmark_set', 'brandingapiconfig_set', 'brandinginfoconfig_set', 'bulkcatalogqueryupdatecommandconfiguration_set', 'bulkchangeenrollmentconfiguration_set', 'bulkemailflag_set', 'bulkunenrollconfiguration_set', 'catalogintegration_set', 'cdnuseragentsconfig_set', 'celebration', 'certificateallowlist_set', 'certificatedateoverride_set', 'certificategenerationcommandconfiguration_set', 'certificategenerationconfiguration_set', 'certificategenerationhistory_set', 'certificatehtmlviewconfiguration_set', 'certificateinvalidation_set', 'check', 'check_password', 'clean', 'clean_fields', 'cohortmembership_set', 'commerceconfiguration_set', 'computegradessetting_set', 'contentlibraries_lti_profile', 'contentlibrarypermission_set', 'contenttypegatingconfig_set', 'cornerstone_transmission_audit', 'cornerstoneglobalconfiguration_set', 'course_groups', 'courseaccessrole_set', 'courseallowpiisharinginltiflag_set', 'courseassetcachettlconfig_set', 'coursedurationlimitconfig_set', 'coursedynamicupgradedeadlineconfiguration_set', 'courseemail_set', 'courseenrollment_set', 'courseenrollmentallowed_set', 'courseentitlement_set', 'courseentitlementsupportdetail_set', 'courseeventbadgesconfiguration_set', 'coursegoal_set', 'coursehlsplaybackenabledflag_set', 'coursemodeexpirationconfig_set', 'courseoverviewimageconfig_set', 'coursepersistentgradesflag_set', 'courseteammembership_set', 'coursevideotranscriptenabledflag_set', 'coursevideouploadsenabledbydefault_set', 'courseyoutubeblockedflag_set', 'crawlersconfig_set', 'credentialsapiconfig_set', 'creditconfig_set', 'csvoperation_set', 'customcourseforedx_set', 'darklangconfig_set', 'dashboardconfiguration_set', 'date_error_message', 'date_joined', 'degreedglobalconfiguration_set', 'delete', 'disableprogresspagestackedconfig_set', 'discountpercentageconfig_set', 'discountrestrictionconfig_set', 'dynamicupgradedeadlineconfiguration_set', 'email', 'email_user', 'embargoedstate_set', 'enrollmentrefundconfiguration_set', 'enterprisefeatureuserroleassignment_set', 'entranceexamconfiguration_set', 'experimentdata_set', 'externalid_set', 'extrainfo', 'first_name', 'flag_set', 'forumsconfig_set', 'from_db', 'full_clean', 'generatedcertificate_set', 'get_all_permissions', 'get_cached', 'get_deferred_fields', 'get_email_field_name', 'get_full_name', 'get_group_permissions', 'get_next_by_date_joined', 'get_previous_by_date_joined', 'get_session_auth_hash', 'get_short_name', 'get_user_permissions', 'get_username', 'globalstatusmessage_set', 'gradereportsetting_set', 'groups', 'has_module_perms', 'has_perm', 'has_perms', 'has_usable_password', 'hlsplaybackenabledflag_set', 'id', 'ignoremobileavailableflagconfig_set', 'instructortask_set', 'integritysignature_set', 'ipfilter_set', 'is_active', 'is_anonymous', 'is_authenticated', 'is_staff', 'is_superuser', 'last_login', 'last_name', 'lastseencoursewaretimezone', 'linkedinaddtoprofileconfiguration_set', 'logentry_set', 'loginfailures_set', 'ltiproviderconfig_set', 'manualenrollmentaudit_set', 'manualverification_set', 'migrateverifiedtrackcohortssetting_set', 'mobileapiconfig_set', 'natural_key', 'normalize_username', 'notifycredentialsconfig_set', 'oauth2_provider_accesstoken', 'oauth2_provider_application', 'oauth2_provider_grant', 'oauth2_provider_refreshtoken', 'oauth2providerconfig_set', 'objects', 'offlinecomputedgrade_set', 'optout_set', 'orgdynamicupgradedeadlineconfiguration_set', 'owned_articles', 'password', 'password_toggle_history', 'pendingemailchange', 'pendingnamechange', 'pendingsecondaryemailchange', 'persistentgradesenabledflag_set', 'photo_verifications_reviewed', 'pk', 'preferences', 'prepare_database_save', 'proctoredexamreviewpolicy_set', 'proctoredexamreviewpolicyhistory_set', 'proctoredexamstudentallowance_set', 'proctoredexamstudentallowancehistory_set', 'proctoredexamstudentattempt_set', 'proctoredexamstudentattempthistory_set', 'profile', 'programenrollment_set', 'programsapiconfig_set', 'providerfilter_set', 'ratelimitconfiguration_set', 'refresh_from_db', 'registration', 'registrationcookieconfiguration_set', 'revisionpluginrevision_set', 'roles', 'samlconfiguration_set', 'samlproviderconfig_set', 'sapsuccessfactorsglobalconfiguration_set', 'save', 'save_base', 'scheduleconfig_set', 'scoreoverrider_set', 'selfpacedconfiguration_set', 'selfpacedrelativedatesconfig_set', 'serializable_value', 'set_password', 'set_unusable_password', 'settings_set', 'simulatecoursepublishconfig_set', 'social_auth', 'softwaresecurephotoverification_set', 'splashconfig_set', 'ssoverification_set', 'sspverificationretryconfig_set', 'standing', 'studentfieldoverride_set', 'studentmodule_set', 'surveyanswer_set', 'systemwideenterpriseuserroleassignment_set', 'systemwideroleassignment_set', 'teams', 'teamsubmission_set', 'transcriptmigrationsetting_set', 'unique_error_message', 'updateroleassignmentswithcustomersconfig_set', 'user_permissions', 'useractivity_set', 'usercalendarsyncconfig_set', 'userdate_set', 'userdemographics', 'username', 'username_validator', 'userpasswordtogglehistory_set', 'userretirementpartnerreportingstatus', 'userretirementrequest', 'userretirementstatus', 'usersignupsource_set', 'userstanding_set', 'usertestgroup_set', 'validate_unique', 'vempipelineintegration_set', 'verified_name_config', 'verifiedname_set', 'verifiednameconfig_set', 'videothumbnailsetting_set', 'videotranscriptenabledflag_set', 'videouploadsenabledbydefault_set', 'waffleflagcourseoverridemodel_set', 'xapi_transmission_audit', 'xblockasidesconfig_set', 'xblockconfiguration_set', 'xblockstudioconfiguration_set', 'xblockstudioconfigurationflag_set', 'xdomainproxyconfiguration_set', 'xmodulestudentinfofield_set', 'xmodulestudentprefsfield_set']
```