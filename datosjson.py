import json
import yaml

with open('/home/devasc/labs/devnet-src/parsing/myfile.json', 'r' ) as json_file:
  ourjson = json.load(json_file)
  print ("Tu Codigo de Token es: {}".format(ourjson['access_token']))
  print ("Tu Token Expira en: {} Segundos".format(ourjson['expires_in']))
  print ("El Nuevo Token es: {}".format(ourjson['refresh_token']))
  print ("El Token vence en:  {} segundos".format(ourjson['refreshtokenexpires_in']))

