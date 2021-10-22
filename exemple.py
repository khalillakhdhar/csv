import csv 
data = [['1'], ['3'], ['5'],['7']] 
file = open('odd.csv', 'w+', newline ='') 
with file:     
    write = csv.writer(file) 
    write.writerows(data) 