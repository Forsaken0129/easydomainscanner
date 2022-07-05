#!/usr/bin/env python3
#https://github.com/Forsaken0129/easydomainscanner
import os

def main():
  print("""
  #######                             ######                                           #####                                                  
 #          ##     ####   #   #      #     #   ####   #    #    ##    #  #    #      #     #   ####     ##    #    #  #    #  ######  #####  
 #         #  #   #        # #       #     #  #    #  ##  ##   #  #   #  ##   #      #        #    #   #  #   ##   #  ##   #  #       #    # 
 #####    #    #   ####     #        #     #  #    #  # ## #  #    #  #  # #  #       #####   #       #    #  # #  #  # #  #  #####   #    # 
 #        ######       #    #        #     #  #    #  #    #  ######  #  #  # #            #  #       ######  #  # #  #  # #  #       #####  
 #        #    #  #    #    #        #     #  #    #  #    #  #    #  #  #   ##      #     #  #    #  #    #  #   ##  #   ##  #       #   #  
 #######  #    #   ####     #        ######    ####   #    #  #    #  #  #    #       #####    ####   #    #  #    #  #    #  ######  #    # 
                                                                                                                                                               
""")

def banner():
	    
	print ("""
\033[1;36m[\033[1;39m1\033[1;36m]\033[1;39m  Easy Domain Scanner
\033[1;36m[\033[1;39m2\033[1;36m]\033[1;39m  Advanced Domain Scanner

""")

def opt_ini():
	
    opt=input("\033[1;39mOption : \033[1;39m")
    #os.chdir('')
    
    
    if(opt == '1'):
	    opt1=input("\n\033[1;39mWebsite For Testing : \033[1;39m")
	    os.system("python3 1.py "+opt1)
	    print(" ")

    if(opt == '2'):
	    os.system("python3 2.py ")
	    print(" ")	    	    		    	    	    	    
    else:
        exit()	   

if __name__ == '__main__':
 main()
banner()
opt_ini()

