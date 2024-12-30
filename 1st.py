def nearest_smallest_and_greatest(arr):
    # Initialize lists to store results
    nearest_smallest = []
    nearest_greatest = []
    
    # Iterate through adjacent pairs
    for i in range(len(arr) - 1):
        # Calculate the sum of the current pair
        pair_sum = arr[i] + arr[i + 1]
        
        # Find nearest smallest
        smaller_candidates = [x for x in arr if x < pair_sum]
        if smaller_candidates:
            nearest_smallest_value = max(smaller_candidates)
        else:
            nearest_smallest_value = None
        
        # Find nearest greatest
        greater_candidates = [x for x in arr if x > pair_sum]
        if greater_candidates:
            nearest_greatest_value = min(greater_candidates)
        else:
            nearest_greatest_value = None
        
        # Append results to lists
        nearest_smallest.append(str(nearest_smallest_value))
        nearest_greatest.append(str(nearest_greatest_value))
    
    return [nearest_smallest, nearest_greatest]

# Example usage
arr = [5, 1, 3, 7]
output = nearest_smallest_and_greatest(arr)
print(output)  # Output: [[5, 3, 7], [7, 5, None]