from scan import *
from colorama import Fore
'''
Pedro Costas - 
Pedro Utida - 
Iago Okuma - 95778
'''




print(f'''{Fore.LIGHTBLUE_EX}
        ____             __     _____                                 
       / __ \____  _____/ /_   / ___/_________ _____  ____  ___  _____
      / /_/ / __ \/ ___/ __/   \__ \/ ___/ __ `/ __ \/ __ \/ _ \/ ___/
     / ____/ /_/ / /  / /_    ___/ / /__/ /_/ / / / / / / /  __/ /    
    /_/    \____/_/   \__/   /____/\___/\__,_/_/ /_/_/ /_/\___/_/     
                                                                  ''')

print(f'''{Fore.LIGHTRED_EX}
    ♠︎ ♣︎ ♥︎ ♦︎ ♠︎ ♣︎ ♥︎ ♦︎ ♠︎ ♣︎ ♥︎ ♦︎ ♠︎ ♣︎ ♥︎ ♦︎ ♠︎ ♠︎ ♣︎ ♥︎ ♦︎ ♠︎ ♣︎ ♥︎ ♦︎ ♠︎ ♣︎ ♥︎ ♦︎ ♠︎ ♣︎ ♥︎ ♦︎  
    ''')

r = int(input(F'''{Fore.LIGHTWHITE_EX}
Tipos de scans:
[ 1 ] - Escanear um range de portas(Lembre-se, cuidado com a quantidade de portas do range, dependendo da quantidade vc pode fazer muito barulho)" 
[ 2 ] - Escanear apenas uma porta. 
Qual tipo de scan você deseja escolher?: '''
))

if r == 1:
    rangeport()
    
else:
    onlyport()