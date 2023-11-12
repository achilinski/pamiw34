from decouple import config
from pamiw3.settings.common import *


DEBUG = False
SECRET_KEY = config('SECRET_KEY')
ALLOWED_HOSTS = ['0.0.0.0', 'localhost', '127.0.0.1']

