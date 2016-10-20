from generator.name_gen import random_string


def test_signup_new_account(app):
    username = random_string('user', 10, symbols=1)
    email = username + "@localhost"
    password = 'test'
    app.james.ensure_user_exists(username,password)
    app.signup.new_user(username, email, password)
    assert app.soap.can_login(username, password)