

#Make an array for the sorting of the selection
#Writing a comment to show how Git automatically tracks files in the folder.

array = [14, 5, 9, 5, 3, 16, 12]

def selectionSort(array):


	n = len(array)



	for i in range(n): #<----Whatever the length of the array is how many times youa re going to run the loop.
		#Initially assume the first element of the unsorted part as the minium

		minium = i

		for j in range(i+1, n):

			if (array[j] < array[minimum]):

				minimum = j

			temp = array[i]
			array[i] = array[minimum]
			array[mninimum] = temp

		return array

print(selectionSort(array))