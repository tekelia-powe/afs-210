def merge_sort(list):
    print("Splitting ",list)
    if len(list)>1:
        middle = len(list)//2
        lhalf = list[:middle]
        rhalf = list[middle:]

        merge_sort(lhalf)
        merge_sort(rhalf)
        a=0
        b=0
        c=0       
        while a < len(lhalf) and b < len(rhalf):
            if lhalf[a] < rhalf[b]:
                list[c]=lhalf[a]
                a=a+1
            else:
                list[c]=rhalf[b]
                b=b+1
            c=c+1

        while a < len(lhalf):
            list[c]=lhalf[a]
            a=a+1
            c=c+1

        while b < len(rhalf):
            list[c]=rhalf[b]
            b=b+1
            c=c+1
    print("Merging ",list)

list = [14,46,43,27,57,41,45,21,70]
merge_sort(list)
print(list)
