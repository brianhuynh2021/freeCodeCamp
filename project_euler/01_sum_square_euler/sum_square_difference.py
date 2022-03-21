def sumsquaredifferent(n):
    squareofn = 0
    squareofsumn = 0
    for i in range(1, n+1):
        squareofn = squareofn + i*i
        squareofsumn = squareofsumn + i
    
    squareofsumn = squareofsumn*squareofsumn
    
    result = squareofsumn - squareofn
    
    return result

result = sumsquaredifferent(100)
print(result)
