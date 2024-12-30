from typing import List

def nearest_smallest_and_greatest(arr: List[int]) -> List[List[str]]:
    nearest_smallest = []
    nearest_greatest = []

    for i in range(len(arr) - 1):
        pair_sum = arr[i] + arr[i + 1]
        
        # Find nearest smallest
        smallest = None
        for num in arr:
            if num < pair_sum:
                if smallest is None or num > smallest:
                    smallest = num
        
        # Append the result for nearest smallest
        nearest_smallest.append(str(smallest) if smallest is not None else "None")
        
        # Find nearest greatest
        greatest = None
        for num in arr:
            if num > pair_sum:
                if greatest is None or num < greatest:
                    greatest = num
        
        # Append the result for nearest greatest
        nearest_greatest.append(str(greatest) if greatest is not None else "None")

    return [nearest_smallest, nearest_greatest]

# Example usage:
arr = [5, 1, 3, 7]
output = nearest_smallest_and_greatest(arr)
print(output)  # Output should be [['5', '3', '7'], ['7', '5', 'None']]