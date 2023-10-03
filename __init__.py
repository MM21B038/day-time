import pip
import importlib
from .requirements import REQUIREMENTS


def import_with_auto_install(package):
    pip.main(['install', package])

for req in REQUIREMENTS:
    import_with_auto_install(req)

from .controller import *
