def convert(seconds): 
    seconds = seconds % (24 * 3600) 
    hours = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
      
    return "%d'hours,%02d'minutes" % (hours, minutes) 
       