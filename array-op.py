#B-11 Pruthviraj Patil
import array as arr
pruthvi = arr.array('i', [1, 2, 3, 4, 5, 6, 7, 7, 9, 10])
print(pruthvi)
print("Length of the array is", len(pruthvi))
print("Occurences of 7",pruthvi.count(7))
pruthvi.insert(2,16)
print(pruthvi)
pruthvi.append(33)
print(pruthvi)
pruthvi.extend([50,51,52])
print(pruthvi)
pruthvi.pop(2)
print(pruthvi)
pruthvi.remove(7)
print(pruthvi)
pruthvi.reverse()
print(pruthvi)
pruthvi.reverse()
print("Index of the element 51 is",pruthvi.index(51)) 