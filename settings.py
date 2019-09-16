import platform

CONNECTION_STRING = ''
DATABASE_NAME = ''

# Template:
# CONNECTION_STRING = 'mysql+pymysql://root:<YourPassword>@localhost/'

# BE ADVISED THAT STORING PASSWORDS IN PLAIN TEXT IS NOT THE BEST WAY!
# THIS WAS DONE FOR THE SHOWCASING AND EASE OF USE PURPOSE.

# Normally this would be done via Environement Variables.

if platform.node() == 'Your_PC_Name':
    CONNECTION_STRING =
    DATABASE_NAME =
else:
    CONNECTION_STRING =
    DATABASE_NAME =
