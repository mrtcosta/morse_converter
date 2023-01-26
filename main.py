import winsound

morse_code = {
    ".": ".-.-.-",
    ",": "--..--",
    "?": "..--..",
    "'": ".----.",
    "!": "-.-.--",
    "/": "-..-.",
    "(": "-.--.",
    ")": "-.--.-",
    "&": ".-...",
    ":": "---...",
    ";": "-.-.-.",
    "=": "-...-",
    '-': "-....-",
    "_": "..--.-",
    '"': ".-..-.",
    '$': "...-..-",
    '@': ".--.-.",
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",

}

text = input("What would you like to convert to morse?\n")


for letter in morse_code.keys():
    text = text.upper().replace(letter, morse_code[letter])

print(f"Your text converted to morse is: {text}")

hear = False
hear_sound = (input("Would you like to hear it? (Y/N) \n")).upper()

if hear_sound == "Y":
    hear = True


while hear:
    for l in text:
        if l == ".":
            frequency = 1000
            duration = 100
        else:
            frequency = 1000
            duration = 300

        winsound.Beep(frequency, duration)
    hear = False

print("Thank you")