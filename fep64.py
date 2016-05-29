def applyToEach(L, f):
	""" Assumes L is a lost, f a function
            Mutates L by replacing each element, e, of L by f(e)"""
    for i in range(len(L)):
        L[i] = f(L[i])
