class CharacterInfo:
    def char_type(character):
        if character.isupper():
            return "Uppercase"
        elif character.islower():
            return "Lowercase"
        else:
            return "Special Character"

user_char = input("Enter a character: ")
print(CharacterInfo.char_type(user_char))