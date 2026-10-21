import os

DEBUG = False
# upload limit in MB
MAX_UPLOAD_MB = int(os.getenv('APP_MAX_UPLOAD_MB', '25'))
