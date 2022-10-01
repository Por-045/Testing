from audioop import reverse


def alternating_characters(text):
    counter = 0
    for i in range(len(text)-1):
        if text[i] == text[i+1]:
            counter += 1
    return counter