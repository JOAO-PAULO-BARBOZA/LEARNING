import random
from datetime import datetime
import time

#esta função diz se um valor é impar ou não
def isOdd(x):
    if(x % 2 == 1):
        return True
    else:
        return False


for i in range(10):
    #reduzi para segundos, assim passa mais rapido.
    right_this_minute = datetime.today().second
    if isOdd(right_this_minute):
        # troquei 'minute' por 'second'
        print("This second seems a little odd.")
    else:
        print("Not an odd second.")
    
    #Deixei apenas entre 1 e 3, para não ficar uma espera tão grande.
    rand = random.randint(1,3)

    #aqui exibe qual foi o tempo em segundos que será esperado.
    print(rand)
    time.sleep(rand)
