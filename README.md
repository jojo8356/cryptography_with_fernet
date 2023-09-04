# cryptography_with_fernet

1. The program begins by importing the Fernet class from the cryptography.fernet library.

2. The generate_key() function generates a new Fernet key by calling Fernet.generate_key(). This key is then saved in a file named "unlock.key" in binary mode ("wb") for later use. The key is also returned by the function.

3. The read_key() function reads the Fernet key from the "unlock.key" file in binary mode ('rb') and returns it.

4. The init_key() function attempts to read the key from the file using read_key(). If the key does not exist (for example, on first run), it generates a new key using generate_key(). Ultimately, the function returns a Fernet object initialized with the retrieved or generated key.

5. The encrypt(txt) function takes a text (txt) as input, initializes a Fernet object using init_key(), then encrypts the text using that Fernet key and returns the encrypted text.

6. The decrypt(encrypted) function takes the encrypted text as input, initializes a Fernet object using init_key(), then decrypts the encrypted text using that Fernet key and returns the decrypted text.
