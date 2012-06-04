from pyres import ResQ
from django.conf import settings
pyres = ResQ(getattr(settings,'PYRES_HOST','localhost:6379'),getattr(settings,'PYRES_PASSWORD',None))

