'''
@author NONO SAHA Cyrille Merleau

Computation of square root 


'''

def nsqrt(n) : 
        
        minsqrt = 0 
        j= n +1
        maxsqrt= perfectSqrt(j)
        while maxsqrt ==0 : 
                maxsqrt = perfectSqrt(j)
                j+=1
                          
        for i in range(2,n+1) : 
                if perfectSqrt(i) !=0 : 
                        minsqrt = perfectSqrt(i) 
        val = (maxsqrt+minsqrt)/2.
        iteration = 1
        while maxsqrt-minsqrt >=0.000000000001: 
                
                if val*val < n : 
                        minsqrt = val
                else : 
                        maxsqrt = val
                val = (maxsqrt+minsqrt)/2.
                iteration+=1 
        
        
        print "Number of iteration is == ", iteration
        return maxsqrt
         

            
def perfectSqrt(n) : 
         
        if n == 1 :
                return 1
        for i in range(2,n+1) : 
                if n%i == 0 :
                        if i ==n/i : 
                                return i
        return 0  
                  
if __name__== "__main__" : 

       print nsqrt(121)
                
                                
