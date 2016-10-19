from django.core.validators import RegexValidator

GLOBAL_ALPHANUMERIC_NAME_VALIDATOR = RegexValidator(
    regex='^[a-zA-Z0-9 _-]*$',
    message="Name must be Alphanumeric. (optional characters: _,-, )",
    code="Invalid company name.")