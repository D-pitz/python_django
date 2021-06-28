A reusable login and registration app styled using bootstrap:

Uses bcrypt to hash and salt the user password before it hits the db.

Validates User email with Email Regex.(other validations apply)

Validation messages are displayed for the user.

To Integrate:  Change the redirect to /success in def user_login() to desired URL.  