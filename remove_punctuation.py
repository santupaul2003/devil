import string

def remove_punctuation(input_string):
    return input_string.translate(str.maketrans('', '', string.punctuation))

if __name__ == "__main__":
    user_input = input("Enter a string: ")
    result = remove_punctuation(user_input)
    print("String without punctuation:", result)
