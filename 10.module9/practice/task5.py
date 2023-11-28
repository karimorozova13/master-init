def format_phone_number(func):
    def inner(phone):
        if len(func(phone)) <12:
            return f'+38{func(phone)}'
        else:
            return f'+{func(phone)}'
    return inner
@format_phone_number
def sanitize_phone_number(phone):
    new_phone = (
        phone.strip()
            .removeprefix("+")
            .replace("(", "")
            .replace(")", "")
            .replace("-", "")
            .replace(" ", "")
    )
    return new_phone

# complicated = format_phone_number(sanitize_phone_number)
print(sanitize_phone_number('0503451234'))