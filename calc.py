>>> python
print("Ti2000")
x = 0
while(x == 0):
    n1 = 0
    n2 = 0
    wer = 0
    ans = "The answer is:"
    a = input("Input anything to initiate.")
    print("Choose an operator.")
    print("1 - Add")
    print("2 - Subtract")
    print("3 - Multiply")
    print("4 - Divide")
    print("5 - Terminate program")
    op = int(input())
    if op == 5:
        print("Terminating Ti2000 program.")
        x = 1
    if x == 0:    
        if op == 1:
         n1 = float(input("Type the first value you want to add."))
         n2 = float(input("Type the second value you want to add."))
         wer = n1 + n2
        if op == 2:
         n1 = float(input("Type the value of the minuend."))
         n2 = float(input("Type the value of the subtrahend."))
         wer = n1 - n2
        if op == 3:
         n1 = float(input("Type the first factor you want to multiply."))
         n2 = float(input("Type the second factor you want to multiply."))
         wer = n1 * n2
        if op == 4:
         n1 = float(input("Type the value of the dividend."))
         n2 = float(input("Type the value of the divisor."))
         wer = n1 / n2
        if op > 4:
            ans = "Nice try."
            wer = "Restarting program..."
        print(ans)
        print(wer)
   
        
  
 
 
   
 
