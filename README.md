# BackEndDevCapstone

## virtual env used was venv -- requirements.txt included

## all tests are in tests.py in app folder

### superuser/admin, does have MySQL privileges

username: admindjango  

password: employee@123!

### Some useful urls for testing

/api/menu/  

/api/booking/  

  -- bookingdate format for JSON  
      "YYYY-MM-DDTHH:mm:ssZ"  
      Z is UTC timezone.  
      For example, America/New_York  
      "2025-01-30T12:00:00-05:00"
  or test using DRF Browsable API.

/api-token-auth/  

  -- to get token, accepts POST calls only.  POST with username and password.  

/auth/users/  

  -- user list, accepts GET and POST.  POST to create new user.  

/auth/users/me/  

  -- this shows current logged-in user.

/api-auth/login/?next=/auth/users/

  -- login.
