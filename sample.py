from operator import itemgetter
import numpy as npy

#English letter frequencies
english_letter_frequencies = [
    [12.00, 'E'], [9.10, 'T'],
    [8.12, 'A'], [7.68, 'O'],
    [7.31, 'I'], [6.95, 'N'],
    [6.28, 'S'], [6.02, 'R'],
    [5.92, 'H'], [4.32, 'D'],
    [3.98, 'L'], [2.88, 'U'],
    [2.71, 'C'], [2.61, 'M'],
    [2.30, 'F'], [2.11, 'Y'],
    [2.09, 'W'], [2.03, 'G'],
    [1.82, 'P'], [1.49, 'B'],
    [1.11, 'V'], [0.69, 'K'],
    [0.17, 'X'], [0.11, 'Q'],
    [0.10, 'J'], [0.07, 'Z']
]

#letter substitution dictionaries
cipher_to_plain = {
    "a": "l", "b": "f",
    "c": "w", "d": "o",
    "e": "a", "f": "y",
    "g": "u", "h": "i",
    "i": "s", "j": "v",
    "k": "z", "l": "m",
    "m": "n", "n": "x",
    "o": "p", "p": "b",
    "q": "d", "r": "c",
    "s": "r", "t": "j",
    "u": "t", "v": "q",
    "w": "e", "x": "g",
    "y": "h", "z": "k",
}

plain_to_cipher = {v: k for k, v in cipher_to_plain.items()}

def calculate_letter_frequencies(text):
    alphabet_list = []
    cipher_len = 0
    for c in text:
        if c.isalpha():
            cipher_len += 1
            if c not in alphabet_list:
                alphabet_list.append(c)

    letter_frequencies = []
    for c in alphabet_list:
        letter_frequencies.append([round(text.count(c) / cipher_len * 100, 2), c])
    
    return letter_frequencies

def decrypt_message(ciphertext, letter_frequencies):
    letter_freq = sorted(letter_frequencies, key=itemgetter(0), reverse=True)
    decrypted_text = ciphertext
    i = 0
    key = []
    
    for f, c in letter_freq:
        print("What letter do you think {} corresponds to in the English language {}.".format(c, english_letter_frequencies[i][1]))
        decrypted_text = decrypted_text.replace(c, english_letter_frequencies[i][1])
        key.append((c, english_letter_frequencies[i][1]))
        i += 1
    
    return decrypted_text, key

def main():
    message = input("Enter message to decrypt: ").lower()
    ciphertext = message
    
    letter_frequencies = calculate_letter_frequencies(ciphertext)
    #print(list(letter_frequencies))

    ip_list = []

    for i in ciphertext:
	    ip_list.append(i)

    ip_set = set(ip_list)
    
    #print (ip_set)
    for j in ip_set:
	    c = ciphertext.count(j)
	    print("[",j,": ",c,"]")
        
    for c in letter_frequencies:
        l = npy.array(english_letter_frequencies)
        if c[1].upper() in l:
            for j in l:
                if c[1].upper() in j:
                    print(c[1], c[0], j[0])
    
    decrypted_text, key = decrypt_message(ciphertext, letter_frequencies)
    print("Key: ", key)
    print("Decrypted Text: {}".format(decrypted_text))

if __name__ == "__main__":
    main()

