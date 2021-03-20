def triangle_area(a,b,c):  
          
    # calculate the semi-perimeter  
    semi = (a + b + c) / 2
      
    # calculate the area  
    area = (semi * (semi - a) * (semi - b) * (semi - c)) ** 0.5
    
    return area
 