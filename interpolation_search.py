def interpolationSearch(A, x):

	# search space is A[left..right]
	(left, right) = (0, len(A) - 1)

	while A[right] != A[left] and A[left] <= x <= A[right]:

		# estimate mid
		mid = left + (x - A[left]) * (right - left) // (A[right] - A[left])

		
		if x == A[mid]:
			return mid


		elif x < A[mid]:
			right = mid - 1


		else:
			left = mid + 1


	if x == A[left]:
		return left


	return -1


if __name__ == '__main__':

	A = [2, 5, 6, 8, 9, 10]
	key = 5

	index = interpolationSearch(A, key)

	if index != -1:
		print("Element found at index", index)
	else:
		print("Element found not in the list")
