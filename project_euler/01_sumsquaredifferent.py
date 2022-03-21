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

# -------------------------------------
# For javascript
# function sumSquareDifference(n) {
#   let sum1 = 0;
#   let sum2 = 0;
#   for(let i = 1;i<=n;i++){
#     sum1 += i*i;
#     sum2 += i;
#   }
#   sum2 = sum2*sum2;
#   return sum2-sum1;
# }

# sumSquareDifference(100);