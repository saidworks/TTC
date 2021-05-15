def countdown(n):
    print(n)
    if n>0:
        countdown(n-1)

countdown(6)

# Divide and conquer => Taking one large data set and dividing it into subsets that we handle independently