def banner():
    print(r'''
==============================================================
        ___                ____         _____ ____    __ 
       /   |  ____  ____  / / /___     / ___// __ \  / / 
      / /| | / __ \/ __ \/ / / __ \    \__ \/ / / / / /  
     / ___ |/ /_/ / /_/ / / / /_/ /   ___/ / /_/ / / /___
    /_/  |_/ .___/\____/_/_/\____/   /____/\___\_\/_____/
          /_/                                       v.1.0
    
     - A lightweight Oracle SQL database Python client -

=============================================================='''                                                          
    )

def menu():
    print(
        '''   SELECT OPTION
==============================================================
 [1] CONNECT TO ORACLE SQL DATABASE
 [2] QUERY DATA
 [3] ALTER DATA
 [4] SETTINGS

 [0] EXIT
==============================================================
'''
    )
    try:
        mode = int(input('> '))
    except:
        pass
    return mode