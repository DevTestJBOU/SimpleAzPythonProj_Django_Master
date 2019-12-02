import os
import sys

i __name__ == '__main__':
i    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'helloworld.settings')
i    try:
i        from django.core.management import execute_from_command_line
i        from django.core.management import execute_from_command_line
          # Bit above duplicated to test SonarCloud 
           # tested already where did not pick up duplicated sections 
           # so trying duplicated lines 
i    except ImportError as exc:
i        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
            "forget to activate a virtual environment?"
           # Bit above duplicated to test SonarCloud 
           # tested already where did not pick up duplicated sections 
           # so trying duplicated lines 

 i       ) from exc

