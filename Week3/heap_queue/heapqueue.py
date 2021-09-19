#import heapq algorithm into the variable heap
import heapq as heap
#given list
list = [25, 35, 22, 85, 14, 65, 75, 22, 58]
print("Original list:")
#print list
print(list)
# Find three largest values
largest = heap.nlargest(3, list)
print("\nThree largest numbers are:", largest)