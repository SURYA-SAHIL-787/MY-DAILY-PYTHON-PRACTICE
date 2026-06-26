class PasswordChecker:
    def __init__(self, password):
        self.password = password

    def check_strength(self):
        has_digit = any(char.isdigit() for char in self.password)
        has_upper = any(char.isupper() for char in self.password)
        has_lower = any(char.islower() for char in self.password)
        has_special = any(not char.isalnum() for char in self.password)

        score = 0

        if len(self.password) >= 8:
            score += 1
        if has_digit:
            score += 1
        if has_upper:
            score += 1
        if has_lower:
            score += 1
        if has_special:
            score += 1

        if score <= 2:
            return "Weak Password"
        elif score <= 4:
            return "Medium Password"
        else:
            return "Strong Password"


password = input("Enter password: ")

checker = PasswordChecker(password)
print(checker.check_strength())
