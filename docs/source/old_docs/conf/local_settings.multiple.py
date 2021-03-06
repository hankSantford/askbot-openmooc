# -*- coding: utf-8 -*-
import saml2
from os import path, environ

BASEDIR = path.dirname(__file__)
#SAML2DIR = path.join(BASEDIR, 'saml2')
COURSES_BASEDIR = '/home/mooc/courses'
SAML2DIR = '/home/mooc/saml2'

#STATIC_ROOT = path.join(environ.get('HOME'), "static_root")
STATIC_ROOT = "/home/mooc/static_root"


LANGUAGE_CODE = 'en'

DEBUG = True #set to True to enable debugging

# STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')
# STATIC_ROOT = '/home/mooc/static-root'

# STATIC_URL = '/m/'#this must be different from MEDIA_URL

DATABASE_NAME_PREFIX = 'askbot_'



#DATABASE_ENGINE = 'mysql' # only postgres (>8.3) and mysql are supported so far others have not been tested yet
#DATABASE_NAME = 'askbot'             # Or path to database file if using sqlite3.
#DATABASE_USER = 'askbot'             # Not used with sqlite3.
#DATABASE_PASSWORD = 'askbot'         # Not used with sqlite3.
#DATABASE_HOST = ''             # Set to empty string for localhost. Not used with sqlite3.
#DATABASE_PORT = ''             # Set to empty string for default. Not used with sqlite3.

ASKBOT_DATABASE_USER = 'askbot'
ASKBOT_DATABASE_PASSWORD = 'askbot'
ASKBOT_DATABASE_ENGINE = 'django.db.backends.mysql'

BOOTSTRAP_MODE = True


SERVER_EMAIL = 'smtp.example.com'
DEFAULT_FROM_EMAIL = 'no-reply@questions.example.com'
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_SUBJECT_PREFIX = ''
EMAIL_HOST = 'smtp.example.com'
EMAIL_PORT = ''
EMAIL_USE_TLS = False



# EXTRA LIVESETTINGS PROPERTIES

EXTRA_SETTINGS = {
    u'APP_COPYRIGHT':'Open Mooc',
    u'USE_LICENSE':'False',
    u'FEEDBACK_SITE_URL': 'https://moocng.org/complaints/'
}

MOOCNG_URL = 'https://moocng.org/'

LANGUAGE_COOKIE_DOMAIN = '.example.com'

FOOTER_LINKS = (
    ('%slegal' % MOOCNG_URL, {
        'en': u'Legal',
        'es': u'Condiciones legales',
    }),
    ('%scopyright' % MOOCNG_URL, {
        'en': u'Moocng Copyright 2012',
        'es': u'Moocng Copyright 2012',
    }),
    ('%stos' % MOOCNG_URL, {
        'en': u'Terms of Use',
        'es': u'Términos de uso',
    }),
    ('%scontact' % MOOCNG_URL, {
        'en': u'Contact',
        'es': u'Contacto',
    }),
)


# saml2 logger
#
LOGGING = {
    'version': 1,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'saml2file': {
           'level': 'DEBUG',
           'class': 'logging.FileHandler',
           'filename': '/tmp/djangosaml2.log',
           'formatter': 'verbose',
        }
    },
    'loggers': {
        'djangosaml2': {
            'handlers': ['saml2file'],
            'level': 'DEBUG',
        }
    }
}



CACHE_BACKEND = 'memcached://127.0.0.1:11211/'
CACHE_PREFIX = 'askbot' #make this unique

SECRET_KEY = 'sdljdfjkldsflsdjkhsjkldgjlsdgfs s '

ASKBOT_URL = ''
BASE_URL = 'http://questions.example.com/'
FULL_ASKBOT_URL = '%s%s' % (BASE_URL, ASKBOT_URL)


# EXTERNAL_KEYS = {u'USE_RECAPTCHA',
#                  u'RECAPTCHA_SECRET':u'6LeJCNYSAAAAAHTzqr4fPu_KsAS4hNXAzlymh8So',
#                  u'RECAPTCHA_KEY':u'asdfasdfasfuiquasui349248951dsi230113411'}

SESSION_EXPIRE_AT_BROWSER_CLOSE = True


SAML_ATTRIBUTE_MAPPING = {
    'mail': ('email', ),
    'cn': ('first_name', ),
    'sn': ('last_name', ),
}

SAML_AUTHORIZATION_ATTRIBUTE = None
SAML_AUTHORIZATION_EXPECTED_VALUE = None

# Closed Forums configuration
#
# SAML_AUTHORIZATION_ATTRIBUTE = "shacUserStatus"
# SAML_AUTHORIZATION_ATTRIBUTE = "schacUserStatus"
# SAML_AUTHORIZATION_EXPECTED_VALUE = "course_name"
# SAML_AUTHORIZATION_URL = "https://idp.example.com/module.php/userregistrationApi/api.php/users/%s?apikey=123456789"
#
# Remember add this to every closed forums or to your skel course_settings
#
# COURSE_CLOSED = True
# SAML_AUTHORIZATION_EXPECTED_VALUE = COURSE_NAME


SAML_CONFIG = {
  # full path to the xmlsec1 binary programm
  'xmlsec_binary': '/usr/bin/xmlsec1',

  # your entity id, usually your subdomain plus the url to the metadata view
  'entityid': '%ssaml2/metadata/' % FULL_ASKBOT_URL,

  # directory with attribute mapping
  'attribute_map_dir': path.join(SAML2DIR, 'attribute-maps'),

  # this block states what services we provide
  'service': {
      # we are just a lonely SP
      'sp' : {
          'name': 'Askbot - OpenMOOC SP',
          'endpoints': {
              # url and binding to the assetion consumer service view
              # do not change the binding or service name
              'assertion_consumer_service': [
                  ('%ssaml2/acs/' % FULL_ASKBOT_URL,
                   saml2.BINDING_HTTP_POST),
                  ],
              # url and binding to the single logout service view
              # do not change the binding or service name
              'single_logout_service': [
                  ('%ssaml2/ls/' % FULL_ASKBOT_URL,
                   saml2.BINDING_HTTP_REDIRECT),
                  ],
              },
          # # This is commented to be compatible with simplesamlphp
          # # attributes that this project need to identify a user
          #'required_attributes': ['uid'],
          #
          # # attributes that may be useful to have but not required
          #'optional_attributes': ['eduPersonAffiliation'],

          # in this section the list of IdPs we talk to are defined
          'idp': {
              # we do not need a WAYF service since there is
              # only an IdP defined here. This IdP should be
              # present in our metadata

              # the keys of this dictionary are entity ids
              'https://idp.example.com/simplesaml/saml2/idp/metadata.php': {
                  'single_sign_on_service': {
                      saml2.BINDING_HTTP_REDIRECT: 'https://idp.example.com/simplesaml/saml2/idp/SSOService.php',
                      },
                  'single_logout_service': {
                      saml2.BINDING_HTTP_REDIRECT: 'https://idp.example.com/simplesaml/saml2/idp/SingleLogoutService.php',
                      },
                  },
              },
          },
      },

 # where the remote metadata is stored
  'metadata': {
      'local': [path.join(SAML2DIR, 'remote_metadata.xml')],
      },

  # set to 1 to output debugging information
  'debug': 1,

  # certificate
  'key_file': path.join("%s%s" % (SAML2DIR, "/certs"), 'server.key'),  # private part
  'cert_file': path.join("%s%s" % (SAML2DIR, "/certs"), 'server.crt'),  # public part


  # own metadata settings
  'contact_person': [
      {'given_name': 'Sysadmin',
       'sur_name': '',
       'company': 'Example CO',
       'email_address': 'sysadmin@example.com',
       'contact_type': 'technical'},
      {'given_name': 'Admin',
       'sur_name': 'CEO',
       'company': 'Example CO',
       'email_address': 'admin@example.com',
       'contact_type': 'administrative'},
      ],
  # you can set multilanguage information here
  'organization': {
      'name': [('Example CO', 'es'), ('Example CO', 'en')],
      'display_name': [('Example', 'es'), ('Example', 'en')],
      'url': [('http://www.example.com', 'es'), ('http://www.example.com', 'en')],
      },
  }

