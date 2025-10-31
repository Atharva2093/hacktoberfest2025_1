def is_palindrome(s):
    processed_s = "".join(s.split()).lower()
    return processed_s == processed_s[::-1]

# --- Input Logic ---
user_string = input("Enter a word or phrase to check if it's a palindrome: ")

if is_palindrome(user_string):
    print(f"'{user_string}' IS a palindrome!")
else:
    print(f"'{user_string}' is NOT a palindrome.")
