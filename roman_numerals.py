def convertToRomanNumerals(n):
    if n > 3999 or n < 1:
        raise Exception("n must be between 1 and 3999.")

    symbols = { 1000 : 'M', 500 : 'D', 100: 'C', 50 : 'L', 10 : 'X', 5 : 'V', 1 : 'I' }

    result = ""
    
    for i in range(3,-1,-1):                  
        k = 0
        a = 10**i
        while n >= a:
            k += 1
            n -= a   

        if k == 4 or k == 9:
            result += symbols[a] + symbols[(k+1)*a]
        elif k >= 5: 
            result +=  symbols[5*a] + symbols[a]*(k-5) 
        else:
            result += symbols[a]*k

    return result


def convertFromRomanNumerals(r):
    symbols =  { 'I' : 1, 'V' : 5, 'X' : 10,  'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000 }
    
    result = 0
    lastSymbol = None
    for symbol in r:
        s = symbols[symbol]
        if lastSymbol and lastSymbol < s:
            result += (s - 2*lastSymbol)
        else:
            result += s
        lastSymbol = s

    return result
