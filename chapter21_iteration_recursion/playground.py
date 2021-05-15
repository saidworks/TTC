def countdown(n):
    print(n)
    if n>0:
        countdown(n-1)

countdown(6)
# check if list or set contain more than one element
    # divide one set to two subsets
    # sort each list
    # compare element of the two lists
        # sort then again in one list
    # return the ordered list (set)
test = [(-i)**i for i in range(50)]

<<<<<<< HEAD
# Divide and conquer => Taking one large data set and dividing it into subsets that we handle independently
=======
def divideAndSort(ensemble):
    if len(ensemble)<2:
        return ensemble
    #create subsets
    else:
        length = len(ensemble) // 2
        ensemble_1 = ensemble[:length]
        ensemble_2 = ensemble[length:]
    for i in range(1,length):
        temp = ensemble_1[i-1]
        if ensemble_1[i] < temp:
            ensemble_1[i-1] = ensemble_1[i]
            ensemble_1[i] = temp
        elif ensemble_1[i] > temp:
            ensemble_1[i] = ensemble_1[i]

    return ensemble_1

print(divideAndSort(test))
>>>>>>> 61c311fedeccb5e2626d101ae30236c58855ee23
