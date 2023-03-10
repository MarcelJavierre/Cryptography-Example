"""
Arquivo responsável por criptografar um DataFrame do pandas.
"""

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import pandas as pd

# Obtém os dados sensíveis
data = pd.DataFrame(((1, 2, 3, 4), (5, 6, 7, 8), (9, 10, 11, 12), (13, 14, 15, 16)))

# Converte os dados sensíveis de DataFrame para string na forma de CSV
dataConverted = data.to_csv()

# Escreve no terminal os dados sensíveis
print("Dados Sensíveis:\n")
print(data)

# Obtém a chave da criptografia
# 32 significa que a chave será de 256 bits
key = get_random_bytes(32)

# Instancia o objeto responsável pela criptografia
cipher = AES.new(key, AES.MODE_EAX)

# Obtém o nonce do objeto responsável pela criptografia
nonce = cipher.nonce

# Criptografa os dados e obtém a tag
cipherText, tag = cipher.encrypt_and_digest(dataConverted.encode("ASCII"))

# Concatena o nonce, a tag e o texto criptografado
# Isto é possível pelo fato do nonce e da tag terem tamanho fixo de 16 bytes
encryptedData = nonce + tag + cipherText

# Salva a chave em um arquivo chamado "key.bin"
with open("key.bin", "wb") as file:
    file.write(key)

# Salva os dados criptografados em um arquivo chamado "encrypted_data.bin"
with open("encrypted_data.bin", "wb") as file:
    file.write(encryptedData)
