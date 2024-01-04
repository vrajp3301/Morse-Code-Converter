MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.',
    'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.',
    'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-',
    'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', ' ': '/'
}
#Creating morse code from text
def text_to_morse(text):
    return ' '.join(MORSE_CODE_DICT.get(char.upper(), char) for char in text)

#Generating text from morse code
def morse_to_text(morse):
    morse_dict = {value: key for key, value in MORSE_CODE_DICT.items()}
    return ''.join(morse_dict.get(code, code) for code in morse.split())


input_text = "Independence Day"
morse_text = text_to_morse(input_text)
print(f"Text to Morse: {morse_text}")

original_text = morse_to_text(morse_text)
print(f"Morse to Text: {original_text}")
