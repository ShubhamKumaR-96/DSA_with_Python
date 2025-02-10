# Given two sorted array merge them and return the array

def merge(l1,l2):
    i=j=0
    merged=[]
    while i<len(l1) and j<len(l2):
        if l1[i]<l2[j]:
            merged.append(l1[i])
            i+=1
        else:
            merged.append(l2[j])
            j+=1

    while i<len(l1):
        merged.append(l1[i])
        i+=1
    while j<len(l2):
        merged.append(l2[j])


    return merged


# Take user input
l1 = list(map(int, input("Enter first sorted list : ").split()))
l2 = list(map(int, input("Enter second sorted list : ").split()))
result=merge(l1,l2)
print("Merged Array : " ,result)
