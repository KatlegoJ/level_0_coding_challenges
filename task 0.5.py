def triangle_area(a,b,c):  
          
    # calculate the semi-perimeter  
    semi_perimeter = (a + b + c) / 2
      
    # calculate the area  
    area = (semi_perimeter * (semi_perimeter - a) * (semi_perimeter - b) * (semi_perimeter - c)) ** 0.5
    
    return area
triangle_area(5, 6, 7)
