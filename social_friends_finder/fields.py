from django.core import validators
from django.db.models.fields import TextField
from django.utils.translation import ugettext_lazy as _
from south.modelsinspector import add_introspection_rules

add_introspection_rules([], ["social_friends_finder\.fields\.CommaSeparatedTextIntegerField"])


class CommaSeparatedTextIntegerField(TextField):
    default_validators = [validators.validate_comma_separated_integer_list]
    description = _("Comma-separated integers")

    def formfield(self, **kwargs):
        defaults = {
            'error_messages': {
                'invalid': _('Enter only digits separated by commas.'),
            }
        }
        defaults.update(kwargs)
        return super(CommaSeparatedTextIntegerField, self).formfield(**defaults)
