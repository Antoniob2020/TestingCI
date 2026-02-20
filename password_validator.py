#Passwor Validator (Unit Testing)


ALLOWED_SPECIALS = set("!@#$%")


def validate_password(pw: str) -> bool:
    # R1: length 8–20 inclusive
    if not isinstance(pw, str):
        return False

    n = len(pw)
    if n < 8 or n > 20:
        return False

    # R3: no spaces
    if " " in pw:
        return False

    # R2: at least 1 letter and at least 1 digit
    has_letter = any(ch.isalpha() for ch in pw)
    has_digit = any(ch.isdigit() for ch in pw)
    if not (has_letter and has_digit):
        return False

    # R4: at least 1 allowed special, and (implicitly) specials must be from the set
    # Our tests enforce that ^ should fail, meaning we treat non-allowed specials as invalid.
    has_allowed_special = any(ch in ALLOWED_SPECIALS for ch in pw)
    if not has_allowed_special:
        return False

    # Reject if any character is a "special" but not in the allowed set.
    # Here we define "special" as any non-letter and non-digit and not space.
    for ch in pw:
        if not ch.isalpha() and not ch.isdigit() and ch != " ":
            if ch not in ALLOWED_SPECIALS:
                return False

    return True
