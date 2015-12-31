from airtng_flask.forms import LoginForm, RegisterForm, VacationPropertyForm
from tests.base import BaseTestCase


class FormTests(BaseTestCase):
    def test_populate_login_form_with_missing_email_should_produce_error(self):
        form = LoginForm(email='', password='')

        assert form.validate() is False
        assert 'E-mail is required' in form.email.errors

    def test_populate_login_form_with_bad_formed_email_should_produce_error(self):
        form = LoginForm(email='email', password='')

        assert form.validate() is False
        assert 'Invalid E-mail address' in form.email.errors

    def test_populate_login_form_with_missing_password_should_produce_error(self):
        form = LoginForm(email='email@email.com', password='')

        assert form.validate() is False
        assert 'Password is required' in form.password.errors

    def test_populate_login_form_with_all_params_should_be_ok(self):
        form = LoginForm(email='email@email.com', password='2323234343434')

        assert form.validate() is True

    def test_populate_register_form_with_missing_params_should_produce_error(self):
        form = RegisterForm(name='Name')

        assert form.validate() is False

    def test_populate_register_form_with_all_params_should_be_ok(self):
        form = RegisterForm(name='Name', email='email@email.com', password='1233', country_code='1',
                            phone_number='4434455555')

        assert form.validate() is True

    def test_populate_vacation_property_form_with_missing_params_should_be_ok(self):
        form = VacationPropertyForm(description='description')

        assert form.validate() is False

    def test_populate_vacation_property_form_with_badformed_url_params_should_produce_error(self):
        form = VacationPropertyForm(description='description', image_url='image.png')

        assert form.validate() is False
        assert 'Invalid Image Url' in form.image_url.errors

    def test_populate_vacation_property_form_with_all_params_should_be_ok(self):
        form = VacationPropertyForm(description='description', image_url='http://images.com/image.png')

        assert form.validate() is True