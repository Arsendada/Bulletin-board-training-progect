from datetime import datetime
from os.path import splitext

from django.template.loader import render_to_string


def get_timestamp_path(instance, filename):
    return '%s%s' % (datetime.now().timestamp(), splitext(filename)[1])


