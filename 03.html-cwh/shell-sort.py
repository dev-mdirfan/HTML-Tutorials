def shellSort(arr, n):
	x=n//2
	while x>0:
		j=x
		while j<n:
			i=j-x
			while i>=0:
				if arr[i+x]>arr[i]:
					break
				else:
					arr[i+x],arr[i]=arr[i],arr[i+x]
				i=i-x
			j+=1
		x=x//2


arrays = [65, 34, 24, 22, 53]
print("input array:",arrays)

shellSort(arrays,len(arrays))
print("sorted array",arrays)
