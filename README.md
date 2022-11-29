## Objective

Simple GUI application that uses Data Encryption Standard (DES) to encrypt or decrypt a 64-bit text using a 64-bit key.

## How it Works

The app simply implements DES Algorithm:

1. First enter a 64-bit text and a 64-bit key both in hex.

2. Choose to either encrypt or decrypt the text.

3. The result of each round's left and right data block and the round key is shown.

4. The final result, which is either the encrypted plain text or the decrypted cipher text, is shown at the buttom.

5. Upon clicking on each round, a new window appears showing the result of that round's steps.

The steps that are shown in each round are:

1. Expansion: Expanding the 32-bit data block into 48-bit data block

2. XORing: XORing the round key with the expanded data

3. S-Box: Substituting bits using 8 S-boxes

4. Permuation: Permuting the data bits

5. XORing: XORing the left data block with the permuted data

6. Final Left data block

7. Final Right data block

8. Round key

Multiple Rounds can be opened together, and they stay opened until closed by the user. Hence, you can see the result of two rounds coming from two different encryptions or decryptions.

## Next Steps

Several steps are to be taken in different aspects of the chat application.

- Encryption Modes: Multiple encryption modes to be available such as AES, classical encryption techniques, stream ciphers, El-Gamal Encryption algorithm, and much more.
- New Features:
  - Exporting the data into an excel sheet.
  - Allowing different input types such as binary input
  - Allowing importing or inserting data which will be divided into data blocks and encrypted
- GUI: Enhancing the GUI furthermore. The GUI right now is made with simple 'tkinter' functions. Hence, it's minimal.
