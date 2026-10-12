"""Шифр Виженера."""


def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.
    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ""
    keyword = keyword.lower()
    if not keyword:
        raise ValueError("Ключ не должен быть пустым")
    for letter in keyword:
        if not "a" <= letter <= "z":
            raise ValueError("В ключе должны быть только английские буквы")

    index = 0
    for letter in plaintext:
        if "a" <= letter <= "z":
            start = ord("a")
        elif "A" <= letter <= "Z":
            start = ord("A")
        else:
            ciphertext += letter
            continue
        shift = ord(keyword[index % len(keyword)]) - ord("a")
        ciphertext += chr(start + (ord(letter) - start + shift) % 26)
        index += 1
    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.
    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ""
    keyword = keyword.lower()
    if not keyword:
        raise ValueError("Ключ не должен быть пустым")
    for letter in keyword:
        if not "a" <= letter <= "z":
            raise ValueError("В ключе должны быть только английские буквы")

    index = 0
    for letter in ciphertext:
        if "a" <= letter <= "z":
            start = ord("a")
        elif "A" <= letter <= "Z":
            start = ord("A")
        else:
            plaintext += letter
            continue
        shift = ord(keyword[index % len(keyword)]) - ord("a")
        plaintext += chr(start + (ord(letter) - start - shift) % 26)
        index += 1
    return plaintext
