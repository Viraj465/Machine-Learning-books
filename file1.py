'''
def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
    
print(fact(5))
'''
'''
def draw_line(tick_length,tick_label=''):
    line = '-'*tick_length
    if tick_label:
        line += ' ' + tick_label
    print(line)

def draw_interval(center_length):
    if center_length > 0:
        draw_interval(center_length - 1)
        draw_line(center_length)
        draw_interval(center_length - 1)

def draw_ruler(num_inches,major_length):
    draw_line(major_length,'0')
    for j in range(1,1+num_inches):
        draw_interval(major_length - 1)
        draw_line(major_length,str(j))

print(draw_ruler(4,4))
'''
'''
data = [2,4,5,7,8,10,12,14,17,19,23,26,28,33,39]
def Binary_search(data,target,low,high):
    if low > high:
        return False
    else:
        mid = (low + high) // 2
        if target == data[mid]:
            return target
        elif target < data[mid]:
            return Binary_search(data,target,low,mid-1)
        else:
            return Binary_search(data,target,mid+1,high)

print(len(data))
print(Binary_search(data,10,0,len(data)-1))
'''

'''
S = [1,2,3,4,5,6]
def reverse(S,start,stop):
    if start<stop-1:
        S[start],S[stop-1] = S[stop-1],S[start]
        reverse(S,start+1,stop-1)
reverse(S,0,len(S))
print(S)
'''

'''def power(x,n):
    if n == 0:
        return 1
    return x*power(x,n-1)
print(power(2,3))
'''
'''
def puzzle_solve(k, S, U):
    # Base case: if k is 1, check if S is a solution
    if k == 1:
        if is_solution(S):
            return [S.copy()]  # Return a copy of S as a solution
        else:
            return []  # Return an empty list if no solution is found

    solutions = []  # List to store solutions

    # Recursive case
    for e in list(U):  # Make a copy of U to avoid modifying it during iteration
        # Add e to the end of S
        S.append(e)
        # Remove e from U
        U.remove(e)

        # Recursively call PuzzleSolve with k-1
        solutions.extend(puzzle_solve(k - 1, S, U))

        # Remove e from the end of S
        S.pop()
        # Add e back to U
        U.add(e)

    return solutions

# Example usage:
def is_solution(S):
    # Replace this with your specific puzzle-solving condition
    return sum(S) == 9

sequence_S = []  # Initial sequence
set_U = {1, 2, 3, 4, 5, 6, 7}  # Initial set of available elements

solutions = puzzle_solve(3, sequence_S, set_U)
print("Solutions found:", solutions)
'''