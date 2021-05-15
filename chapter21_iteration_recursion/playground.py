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
test = [i*i for i in range(50)]


# Divide and conquer => Taking one large data set and dividing it into subsets that we handle independently
def divideAndSort(ensemble):
    if len(ensemble)<2:
        return ensemble
    #create subsets
    else:
        length = len(ensemble) // 2
        L1 = ensemble[:length]
        L2 = ensemble[length:]
        i = 0
        j = 0
        k = 0
        while (j < len(L1)) or (k < len(L2)):
            if j < len(L1):
                if k < len(L2):
                    # we are not at the end of L1 or L2, so pull the smaller value
                    if L1[j] < L2[k]:
                        ensemble[i] = L1[j]
                        j += 1
                    else:
                        ensemble[i] = L2[k]
                        k += 1
                else:
                    # we are at the end of L2, so just pull from L1
                    ensemble[i] = L1[j]
                    j += 1
            else:
                # we are at the end of L1, so just pull from L2
                ensemble[i] = L2[k]
                k += 1
            i += 1
        return ensemble

# Quick Sort
    #pick the pivot
    #form two list one (L1) with number bigger than pivot and (L2) other less than it
    #quick sort L1 and L2
    #join two list and pivot
import random
def quickSort(L):
    if len(L) < 2:
        return L
    else:
        index = random.randint(0,len(L)//2)
        pivot = L[index]
        L1 = [i for i in L if i<pivot]
        L2 = [i for i in L if i>pivot]
    quickSort(L1)
    quickSort(L2)
    L = L1
    L.append(pivot)
    L.extend(L2)
    return L
print(quickSort(test))
