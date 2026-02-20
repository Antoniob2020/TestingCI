#Test Password Validator


import unittest

from password_validator import validate_password


class TestValidatePassword(unittest.TestCase):
    # R1: length 8–20 inclusive
    def test_rejects_too_short(self):
        self.assertFalse(validate_password("Ab1!xxx"))  # 7 chars (SHOULD FAIL)

    def test_accepts_min_length(self):
        self.assertTrue(validate_password("Ab1!xxxx"))  # 8 chars (SHOULD PASS)

    def test_accepts_max_length(self):
        pw = "Ab1!" + "x" * 16  # total 20
        self.assertTrue(validate_password(pw))  # (SHOULD PASS)

    def test_rejects_too_long(self):
        pw = "Ab1!" + "x" * 17  # total 21
        self.assertFalse(validate_password(pw)) # (SHOULD FAIL)


    # R2: at least 1 letter and at least 1 digit
    def test_rejects_no_digit(self):
        self.assertFalse(validate_password("Abcdefg!"))  # has letter, no digit

    def test_rejects_no_letter(self):
        self.assertFalse(validate_password("1234567!"))  # has digit, no letter


    # R3: no spaces
    def test_rejects_spaces(self):
        self.assertFalse(validate_password("Ab1!xx x"))  # contains space

    # R4: includes at least 1 special from !@#$%
    def test_rejects_missing_required_special(self):
        self.assertFalse(validate_password("Ab1xxxxx"))  # no special from set

    def test_accepts_with_required_special(self):
        self.assertTrue(validate_password("Ab1@xxxx"))  # @ is allowed

    def test_rejects_special_not_in_allowed_set(self):
        # Requirement says special must be from !@#$% specifically
        self.assertFalse(validate_password("Ab1^xxxx"))  # ^ not allowed


if __name__ == "__main__":
    unittest.main()
