def compute_items(x):
    # x =[3,5,7,9,2]*/

    sum = 0
    for i in x:
     if isinstance(i,int):
      sum += i 
     elif isinstance(i,list):
      sum+=compute_items(i)

    return (sum)
 
print(compute_items([3,5,7,9,2,[1,7,2]]))
