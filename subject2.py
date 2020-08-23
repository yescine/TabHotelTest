def isMultipleOfN(num): 
      
    while ( num > 0 ): 
        num = num - 3
  
    if ( num == 0 ): 
        return True
  
    return False

print(isMultipleOfN(10))