#WAF to convert temperature from celcius to fahrenheit

# formula c = 5*(f-32)/9

def f_to_c(f):
    
    return 5*(f-32)/9
f = int(input("enter the temperature :"))
c = f_to_c(f)
print(f"{round(c , 2)} °C")



