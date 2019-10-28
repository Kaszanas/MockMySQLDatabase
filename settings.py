import platform
import os

driver_string = 'mysql+pymysql'
username = 'root'

'''
Template:
CONNECTION_STRING = 'mysql+pymysql://username:password@localhost/'
If there is a port required for connection it will look like this:
CONNECTION_STRING = 'mysql+pymysql://username:password@localhost:port/'

REMEMBER:
Before using this script You will need to add Your password to the Environment Variables.
You can either do it in Your system settings or using the console.
'''

if platform.node() == 'Your_PC_Name':
    CONNECTION_STRING = f'{driver_string}://{username}:{os.environ.get("DB_PASSWORD")@localhost/}'
    DATABASE_NAME = 'Database'
else: # If You wouldn't like to specify the PC name.
    CONNECTION_STRING =
    DATABASE_NAME =
