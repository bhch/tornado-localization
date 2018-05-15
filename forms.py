from wtforms import Form, StringField
from wtforms.validators import ValidationError
from speaklater import make_lazy_gettext



class TestForm(Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._ = make_lazy_gettext(lambda: self.meta.locale.translate)

    # fields
    username = StringField('Username')

    class Meta:
        locale = None

    def validate_username(self, field):
        raise ValidationError(self._("Enter a valid value."))