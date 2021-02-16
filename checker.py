def getInvCount(arr) :
 
    inv_count = 0
    for i in range(0, len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j] and arr[j] != 0:
                inv_count += 1

    return inv_count
     
# This function returns true 
# if given 8 puzzle is solvable. 
def isSolvable(puzzle) : 
 
    # Count inversions in given 8 puzzle 
    invCount = getInvCount(puzzle)
   
    # return true if inversion count is even. 
    return (invCount % 2 == 0)
     
    # Driver code
puzzle = [5,2,8,4,1,7,0,3,6] 
if(isSolvable(puzzle)) : 
    print("Solvable")
else :
    print("Not Solvable")
     
# This code is contributed by https://www.linkedin.com/in/henrique-conte-7b2283180/,  https://www.linkedin.com/in/pedro-henrique-pons-fiorentin-984b38201/ and https://www.linkedin.com/in/gabriel-vogel-pinto-366323196/

