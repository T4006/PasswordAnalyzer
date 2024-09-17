import re

class PasswordAnalyzer:
    def __init__(self):
        self.common_patterns = ["123", "abc", "password", "qwerty"]  # Common weak patterns
        self.common_words = ["password", "123456", "admin", "letmein"]  # Common weak words

    def evaluate_strength(self, password):
        length = len(password)
        complexity = self.calculate_complexity(password)
        entropy = self.calculate_entropy(password)

        return length, complexity, entropy

    def check_weakness(self, password, username):
        weaknesses = []

        # Check for common weak patterns
        for pattern in self.common_patterns:
            if pattern in password.lower():
                weaknesses.append("Contains a common weak pattern")

        # Check for common weak words
        for word in self.common_words:
            if word in password.lower():
                weaknesses.append("Contains a common weak word")

        # Check for variations of username
        if username.lower() in password.lower():
            weaknesses.append("Contains variations of the username")

        return weaknesses

    def recommend_strength(self, password):
        recommendations = []

        # Check length
        if len(password) < 8:
            recommendations.append("Increase the length of the password")

        # Check for complexity
        if not any(char.isdigit() for char in password):
            recommendations.append("Include numbers (e.g., 0-9)")
        if not any(char.isalpha() for char in password):
            recommendations.append("Include letters (e.g., a-z)")
        if not any(char.isupper() for char in password):
            recommendations.append("Include uppercase letters (e.g., A-Z)")
        if not any(char.islower() for char in password):
            recommendations.append("Include lowercase letters (e.g., a-z)")
        if not any(char in "!@#$%^&*()-_+=<>,.?/:;{}[]|~" for char in password):
            recommendations.append("Include special characters (e.g., !@#$%^&*)")

        return recommendations

    def calculate_complexity(self, password):
        # A simple measure of complexity could be the number of unique characters
        return len(set(password))

    def calculate_entropy(self, password):
        # Calculate entropy based on the length and complexity of the password
        # This is a simplistic calculation and may not represent true entropy
        return len(password) * self.calculate_complexity(password)

    
def main():
    analyzer = PasswordAnalyzer()
    print(r""".-. .-. .-. .-.   .-. . . .-. .   . . .-. .-. .-. 
|-' |-| `-. `-.   |-| |\| |-| |    |   /  |-  |(  
'   ` ' `-' `-'   ` ' ' ` ` ' `-'  `  `-' `-' ' ' """)
    # User input
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    # Evaluate strength
    length, complexity, entropy = analyzer.evaluate_strength(password)
    print("Password length:", length)
    print("Password complexity:", complexity)
    print("Password entropy:", entropy)

    # Check weaknesses
    weaknesses = analyzer.check_weakness(password, username)
    if weaknesses:
        print("Weaknesses detected:")
        for weakness in weaknesses:
            print("-", weakness)

    # Recommend improvements
    recommendations = analyzer.recommend_strength(password)
    if recommendations:
        print("Recommendations:")
        for recommendation in recommendations:
            print("-", recommendation)
    
    # Check password is secure or not yet.
    if length >= 12 and complexity >= 10 and entropy >= 120:
        print("Password is secure!")
    else:
        print("Password is not yet secure.")

if __name__ == "__main__":
    main()
