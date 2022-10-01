def funny_string(text):
    
    ascii_text = [ord(i) for i in text]
    reversed_ascii_text = ascii_text[::-1]

    ascii_text_differnce = [abs(ascii_text[i] - ascii_text[i+1]) for i in range(len(ascii_text)-1)]
    reversed_ascii_text_differnce = [abs(reversed_ascii_text[i] - reversed_ascii_text[i+1]) for i in range(len(reversed_ascii_text)-1)]

    if ascii_text_differnce == reversed_ascii_text_differnce:
        return "Funny"
    return "Not Funny"