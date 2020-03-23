activate_this = 'C:/AAA/coding/_practice/www-test/test-venv/Scripts/activate_this.py'
# execfile(activate_this, dict(__file__=activate_this))
exec(open(activate_this).read(),dict(__file__=activate_this))

import os
import sys
import site

# Add the site-packages of the chosen virtualenv to work with
site.addsitedir('C:/AAA/coding/_practice/www-test/test-venv/Lib/site-packages')




# Add the app's directory to the PYTHONPATH
sys.path.append('C:/AAA/coding/_practice/www-test/test-venv/Scripts/testp_project')
sys.path.append('C:/AAA/coding/_practice/www-test/test-venv/Scripts/testp_project/testp_project')

os.environ['DJANGO_SETTINGS_MODULE'] = 'testp_project.settings'
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "testp_project.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()