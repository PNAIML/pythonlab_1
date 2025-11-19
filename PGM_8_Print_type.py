a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
add=a+b
sub=a-b
mult=a*b
div=a/b
mod=a%b
print("ADD:",add)
print("Sum: {0}, Diff: {1}, Mult: {2}, Div:{3}, Mod:{4}".format(add,sub,mult,div,mod)) #Print using Format

print("Sum: %d, Diff: %d, Mult: %d, Div:%15.4f, Mod:%d"%(add,sub,mult,div,mod)) #Print using PADDING & PRECISION

print('{0:<4} | {1:^4} | {2:^4} | {3:>4}'.format('Sum','Diff','Mult','Div'))
print('{0:<4} | {1:^4} | {2:^4} | {3:>4}'.format(add,sub,mult,div))
