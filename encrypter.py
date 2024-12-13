import os
import pyaes

# Recebe o arquivo a ser encriptado
print( "Informe o caminho do arquivo a ser encriptado: ")
file_path = str(input())

# Abre o arquivo a ser encriptado
file = open(file_path, "rb")
file_data = file.read()
file.close()

# Coleta a chave da criptografia
print("Informe a chave de criptografia (16 bytes): ")
keyText = str(input())
key = keyText.encode()
aes = pyaes.AESModeOfOperationCTR(key)

# Criptografa os dados do arquivo
crypt_data = aes.encrypt(file_data)

# Salva em um novo arquivo com a extensão .encrypted
crypt_file = file_path + ".encrypted"
crypt_file = open(crypt_file, "wb")
crypt_file.write(crypt_data)
crypt_file.close()

# Remove o arquivo 
os.remove(file_path)
