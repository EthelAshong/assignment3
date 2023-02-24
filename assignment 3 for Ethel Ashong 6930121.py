#script for buying  a car 
#this code belongs to 6930121
print('Welcome to Ethel Cars')

carSelection={"Tesla":250,"Jeep":300,"Hyundai":450,"Chevrolet":180,"Kia":950,"Toyota":450,"Honda":700, \
 "Ford":700,"BMW":339,"Mercedes-Benz":760,"Ferrari":660,"Porshe":990,"Bentley":554,"Subaru":668,"Jaguar":654,\
"Mazda":865,"Nissan":437,"Bugatti":332,"Acura":556,"Astorn Martin":778,"Volkswagen":875,"Volvo":667,"Mclaren":990,\
 "Lincoln":624,"Genesis":889,"Lotus":990,"Diamler":941,"Peugot":999,"Mini":554,"Fiat":225,"Pontiac":556}
    
buy=input('Do you want to buy a car? yes/no \n ').strip()

if buy.lower()=='yes':
    print('These are the available car models and prices:\n')
    
    print([carSelection])
    
    carName=input('Which of the cars do you want to buy \n').strip()
    
    if carName in carSelection:
        print(f'You have bought {carName} at {carSelection[carName]} dollars\n')
        
        print('Thank you for shopping with Ethel cars.See you next time')
else:
    print('Thank you for contacting Ethel cars.Sorry for any inconveniences caused')
    
    

 


    