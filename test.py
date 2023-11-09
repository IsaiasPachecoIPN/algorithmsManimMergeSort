def merge_sort(arr, step_dict=None, step_key=''):
    if step_dict is None:
        step_dict = {}

    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half, step_dict, step_key + 'L')
        merge_sort(right_half, step_dict, step_key + 'R')

        # Merge the two halves
        merged_arr = []
        i = j = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                merged_arr.append(left_half[i])
                i += 1
            else:
                merged_arr.append(right_half[j])
                j += 1

        merged_arr.extend(left_half[i:])
        merged_arr.extend(right_half[j:])

        # Store the intermediate result in the dictionary
        step_dict[step_key] = merged_arr

    return step_dict

# Example usage
input_array = [5,2,4,7,1,3,2,8]
result_dict = merge_sort(input_array)

# Print the result dictionary
for key, value in result_dict.items():
    print(f"{key}: {value}")