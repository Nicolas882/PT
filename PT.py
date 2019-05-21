# -*- coding: utf-8 -*-
"""
Created on Sun May 10 20:25:23 2019

@author: JC
"""
#Encriptar el mensaje
import smtplib
import Crypto
import binascii

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

random_generator = Crypto.Random.new().read

private_key = RSA.generate(1024, random_generator)
public_key = private_key.publickey()

private_key = private_key.exportKey(format = 'DER')
public_key = public_key.exportKey(format = 'DER')

private_key = binascii.hexlify(private_key).decode('utf8')
public_key = binascii.hexlify(public_key).decode('utf8')

private_key = RSA.importKey(binascii.unhexlify(private_key))
public_key = RSA.importKey(binascii.unhexlify(public_key))

mensaje = input(str("Inserte el mensaje a encriptar: "))
mensaje = mensaje.encode()

cipher = PKCS1_OAEP.new(public_key)
encrypted_message = cipher.encrypt(mensaje)

print("\nNuestro mensaje encriptado:", encrypted_message)
print("\nNuestra llave privada:", private_key)
print("\nNuestra llave publica:", public_key)

#Desencriptar el mensaje
cipher = PKCS1_OAEP.new(private_key)
mensaje = cipher.decrypt(encrypted_message)
print("\nMensaje desencriptado: ", mensaje)

mensaje2 = "Mensaje encriptado: "

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login('jc1095927@gmail.com', 'rteuKKn7yfPYKdb')

server.sendmail('jc1095927@gmail.com', 'jc1095927@gmail.com', encrypted_message)

print("\nEl correo se envio de forma exitosa")

server.quit()


