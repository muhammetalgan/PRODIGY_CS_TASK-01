# -*- coding: utf-8 -*-
"""
Prepared by Muhammet ALGAN for Internship task-01 on 1.03.2024

"""

import tkinter as tk
from tkinter import messagebox

def remove_spaces(text):
    return ''.join(text.split())

def is_english(text):
    return all(char.isalpha() and char.lower() in 'abcdefghijklmnopqrstuvwxyz' for char in text)

def encryption(plainText, shiftValue):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_text = ""
    for char in plainText:
        if char.lower() in alphabet:
            index = alphabet.index(char.lower())
            new_index = (index + shiftValue) % 26
            encrypted_text += alphabet[new_index]
        else:
            encrypted_text += char
    return encrypted_text

def decryption(ciphertext, shiftValue):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    decrypted_text = ""
    for char in ciphertext:
        if char.lower() in alphabet:
            index = alphabet.index(char.lower())
            new_index = (index - shiftValue) % 26
            decrypted_text += alphabet[new_index]
        else:
            decrypted_text += char
    return decrypted_text

def encrypt_button_click():
    plain_text = remove_spaces(entry_text.get("1.0", tk.END).strip())
    shift_value = entry_shift.get()
    if is_english(plain_text) and shift_value.isdigit():
        shift_value = int(shift_value)
        encrypted_text = encryption(plain_text, shift_value)
        text_output.delete("1.0", tk.END)
        text_output.insert(tk.END, encrypted_text)
    else:
        messagebox.showerror("Error", "Please enter only English alphabet characters for text and numerical digits for shift value.")

def decrypt_button_click():
    cipher_text = remove_spaces(entry_text.get("1.0", tk.END).strip())
    shift_value = entry_shift.get()
    if is_english(cipher_text) and shift_value.isdigit():
        shift_value = int(shift_value)
        decrypted_text = decryption(cipher_text, shift_value)
        text_output.delete("1.0", tk.END)
        text_output.insert(tk.END, decrypted_text)
    else:
        messagebox.showerror("Error", "Please enter only English alphabet characters for text and numerical digits for shift value.")

# GUI oluşturma
root = tk.Tk()
root.title("ALGAN - Caesar Cipher Encryption and Decryption")

label_text = tk.Label(root, text="Enter text:", font=("Helvetica", 12))
label_text.grid(row=0, column=0, sticky="w", padx=10, pady=5)

entry_text = tk.Text(root, height=5, width=30, font=("Helvetica", 12))
entry_text.grid(row=0, column=1, padx=10, pady=5)

label_shift = tk.Label(root, text="Enter shift value:", font=("Helvetica", 12))
label_shift.grid(row=1, column=0, sticky="w", padx=10, pady=5)

entry_shift = tk.Entry(root, font=("Helvetica", 12))
entry_shift.grid(row=1, column=1, padx=10, pady=5)

encrypt_button = tk.Button(root, text="Encrypt", command=encrypt_button_click, font=("Helvetica", 12))
encrypt_button.grid(row=2, column=0, pady=10)

decrypt_button = tk.Button(root, text="Decrypt", command=decrypt_button_click, font=("Helvetica", 12))
decrypt_button.grid(row=2, column=1, pady=10)

text_output = tk.Text(root, height=5, width=30, font=("Helvetica", 12))
text_output.grid(row=3, columnspan=2, padx=10, pady=5)

root.mainloop()
