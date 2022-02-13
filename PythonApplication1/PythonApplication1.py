import imp
import random
from time import *
from var import *
import fun


print('''
      
      Milyoncu Oyununa Xos Gelmisiniz
      Cavab vermek ucun konsola varianti yazin
      Jokerden istifade etmek ucun konsola J yazin
      Cixis etmek ucun konsola K yazin
      
      Oyun Baslayir
      ''')
fun.loading()

def panel():
    print(f'''
        
            ##################################################
        
                        Sualin Deyeri:{q[3]}
        
            {que.index(q)+1}){q[0]}
        
        A){a}                       B){b}
            
        C){c}                       D){d}
              
            ##################################################
          ''')

for q in que:
    random.shuffle(q[1])
    a = q[1][0]
    b = q[1][1]
    c = q[1][2]
    d = q[1][3]
    panel()
    answer = str(input('Cavab: '))
    
    #Cavabin Joker olub olmadigini yoxluyur
    if answer.lower() == 'j':
        while True:
            print(
            f'''
            1.50/50
            2.Dosta zeng
            3.Xalqa muraciet
            0.Cixis
            ''')
            choice = int(input('Seciminiz: '))
            if choice == 1 and j1:
                if a == q[2]:
                    b = ''
                    d = ''
                elif b == q[2]:
                    a = ''
                    c = ''
                elif c == q[2]:
                    a = ''
                    d = ''
                elif d == q[2]:
                    b = ''
                    c = ''
                j1 = False
                panel()
                answer = str(input('Cavab: '))
                if answer.lower() == 'j':
                    continue
                else:
                    break
            elif choice == 2 and j2:
                print(f'Dostunuzun cavabi: {q[2]}')
                j2 = False
                panel()
                answer = str(input('Cavab: '))
                if answer.lower() == 'j':
                    continue
                else:
                    break
            elif choice == 3 and j3:
                j3 = False
                ja = jb = jc = jd = 0
                for i in range(100):
                    ran = random.choice(['A', 'B', 'C', 'D'])
                    if ran == 'A':
                        ja += 1
                    elif ran == 'B':
                        jb += 1
                    elif ran == 'C':
                        jc += 1
                    elif ran == 'D':
                        jd += 1
                print(f'''
                    Xalqin secimi:
                    A-{ja}%   B-{jb}%   C-{jc}%   D-{jd}%
                    ''')
                panel()
                answer = str(input('Cavab: '))
                if answer.lower() == 'j':
                    continue
                else:
                    break
            elif choice == 0:
                panel()
                answer = str(input('Cavab: '))
                if answer.lower() == 'j':
                    continue
                else:
                    break
            else:
                print('Bu joker 1 defe istifade edilib')
    
    #String olan cavabimizi variable'a cevirir
    if answer.lower() == 'a':
        answer = a
    elif answer.lower() == 'b':
        answer = b
    elif answer.lower() == 'c':
        answer = c
    elif answer.lower() == 'd':
        answer = d
    
    #Cavabin dogrulugunu yoxlamaq
    if answer== q[2]:
        balance = q[3]
        print(f'Duzgun Cavab.Hazirki balansiniz:{balance}')
        
        #Baraj suali olub olmadigini yoxlayir
        if answer == q[2] and que.index(q) == 4:
            bar1 = True
        elif answer == q[2] and que.index(q) == 9:
            bar1 = False
            bar2 = True
    elif answer.lower() == 'k':
        print(f'Yarisdiginiz ucun tesekkurler.Qazandiginiz miqdar {balance}')
        break
    else:
        if bar1:
            balance = 1000
        elif bar2:
            balance = 32000
        else:
            balance = 0
        print(f'Yarisdiginiz ucun tesekkurler sizin balansiniz: {balance}')
        break
    
    if balance==1000000:
        print('Tebrikler siz milyoncu adina layiq oldunuz.')
        break
    
        
            
    
