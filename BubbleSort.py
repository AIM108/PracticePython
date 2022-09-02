numbers = [10,29,9,0,1];

flag=False
while(flag==False):
    flag=True
    for x in numbers:
        pointerA=numbers.index(x)
        pointerB=pointerA+1
        while(pointerB != len(numbers)):
            if(numbers[pointerA]>numbers[pointerB]):
                tempObject=numbers[pointerA]
                numbers[pointerA]=numbers[pointerB]
                numbers[pointerB]=tempObject
                flag=False
            pointerA=pointerA+1
            pointerB=pointerB+1
            print(numbers)    
    
