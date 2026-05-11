from cryptography.hazmat.primitives.ciphers.aead import AESGCM

print(",--.    ,-----.      ,--.,--.      ,---.  ,------. ,--.")
print("|  |   '  .-.  '     |  ||  |     /  O  \ |  .--. '|  |  ___________")
print("|  |   |  | |  |,--. |  ||  |    |  .-.  ||  '--' ||  | | decryptor |")
print("|  '--.'  '-'  '|  '-'  /|  |    |  | |  ||  | --' |  | '-----------'")
print("`-----' `-----'  `-----' `--'    `--' `--'`--'     `--'   -nghya-")


def decrypt_file(input_file, key_file):
    # Đọc khóa từ file
    with open(key_file, "rb") as f:
        key = f.read()
    aesgcm = AESGCM(key)

    with open(input_file, 'rb') as f:
        file_data = f.read()

    nonce = file_data[:12]
    ext_len = file_data[12]
    ext = file_data[13:13+ext_len].decode()
    encrypted_data = file_data[13+ext_len:]

    decrypted_data = aesgcm.decrypt(nonce, encrypted_data, None)

    output_file = "restored" + ext
    with open(output_file, 'wb') as f:
        f.write(decrypted_data)

    print(f"Decryption completed, restored file: {output_file}")

if __name__ == "__main__":
    enc_file = input("Fill your encrypted file name: ")
    decrypt_file(enc_file, "key.bin")
