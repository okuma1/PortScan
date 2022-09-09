import logging
from pickletools import read_int4
import nmap
from logging import info, basicConfig, INFO

basicConfig(
    level=INFO,
    filename='c:/Users/iago_/Desktop/vscode/cp/github/hostEscaneados.txt',
    filemode='a',
    encoding='UTF-8',
    format="Data do Scan:%(asctime)s|%(levelname)s:%(message)s"
)

def rangeport():
  ip = input("IP do alvo: ")
  porta = input("Range de portas(Pstart-Pstop): ")
  i=nmap.PortScanner()
  scan = i.scan(ip, porta, arguments="-Pn -v -A -sC")
  #print(i[ip].keys())
  #print(i[ip]['addresses'])
  print('-'*50)
  print(("Host: {}".format(i[ip]['addresses']['ipv4'])))
  try:
    mac = i[ip]['addresses']['mac']
    print("Mac Addresses: {}".format(i[ip]['addresses']['mac']))
    print(("Info do Host: {}".format(i[ip]['vendor'][mac])))
  except:
    r =("O Mac addresses do host não encontrado.")
    print(r)
  print("Nome do Host(máquina): {}".format(i[ip].hostname()))
  print(("Estado da conexão: {}".format(i[ip]['status']['state'])))
  print(("Versão do Kernel: {}".format(i[ip]['osmatch'][0]['name'])))

  #LOG
  try:
    info("\nHost:{}\nMac Addresses:{}\nNome do Host(máquina):{}\nInfo do Host:{}\nEstado da conexão:{}\nVersão do Kernel:{}".format(i[ip]['addresses']['ipv4'], i[ip]['addresses']['mac'], i[ip].hostname(), i[ip]['vendor'][mac], i[ip]['status']['state'], i[ip]['osmatch'][0]['name']))
  except:
    info("\nHost:{}\nMac Addresses:{}\nNome do Host(máquina):{}\nEstado da conexão:{}\nVersão do Kernel:{}".format(i[ip]['addresses']['ipv4'],r , i[ip].hostname(), i[ip]['status']['state'], i[ip]['osmatch'][0]['name']))

  for proto in i[ip].all_protocols():
    print("Protocolo:{} ".format(proto))
    ports = i[ip][proto].keys()
    for port in ports: 
      print("♠︎ ♣︎ ♥︎ ♦︎ "*5)
      print("Porta({}): {}|{} - Versão: {}|{}".format(i[ip][proto][port]['state'], port, i[ip][proto][port]['name'], i[ip][proto][port]['version'], i[ip][proto][port]['product']))
      info("Porta({}): {}|{} - Versão: {}|{}".format(i[ip][proto][port]['state'], port, i[ip][proto][port]['name'], i[ip][proto][port]['version'], i[ip][proto][port]['product']))
      

def onlyport():
  ip = input("IP do alvo: ")
  porta = input("Porta: ")
  i=nmap.PortScanner()
  scan = i.scan(ip, porta, arguments="-Pn -v -A -sC")
  #print(i[ip].keys())
  #print(i[ip]['addresses'])
  print('-'*50)
  print(("Host: {}".format(i[ip]['addresses']['ipv4'])))
  try:
    mac = i[ip]['addresses']['mac']
    print("Mac Addresses: {}".format(i[ip]['addresses']['mac']))
    print(("Info do Host: {}".format(i[ip]['vendor'][mac])))
  except:
    r =("O Mac addresses do host não encontrado.")
    print(r)
  print("Nome do Host(máquina): {}".format(i[ip].hostname()))
  print(("Estado da conexão: {}".format(i[ip]['status']['state'])))
  print(("Versão do Kernel: {}".format(i[ip]['osmatch'][0]['name'])))

  #Log
  try:
    info("\nHost:{}\nMac Addresses:{}\nNome do Host(máquina):{}\nInfo do Host:{}\nEstado da conexão:{}\nVersão do Kernel:{}".format(i[ip]['addresses']['ipv4'], i[ip]['addresses']['mac'], i[ip].hostname(), i[ip]['vendor'][mac], i[ip]['status']['state'], i[ip]['osmatch'][0]['name']))
  except:
    info("\nHost:{}\nMac Addresses:{}\nNome do Host(máquina):{}\nEstado da conexão:{}\nVersão do Kernel:{}".format(i[ip]['addresses']['ipv4'], r, i[ip].hostname(), i[ip]['status']['state'], i[ip]['osmatch'][0]['name']))


  for proto in i[ip].all_protocols():
    print("Protocolo:{} ".format(proto))
    ports = i[ip][proto].keys ()
    for port in ports: 
        print("♠︎ ♣︎ ♥︎ ♦︎ "*5)
        print("Porta({}): {}|{} - Versão: {}|{}".format(i[ip][proto][port]['state'], port, i[ip][proto][port]['name'], i[ip][proto][port]['version'], i[ip][proto][port]['product']))
        info("Porta({}): {}|{} - Versão: {}|{}".format(i[ip][proto][port]['state'], port, i[ip][proto][port]['name'], i[ip][proto][port]['version'], i[ip][proto][port]['product']))

