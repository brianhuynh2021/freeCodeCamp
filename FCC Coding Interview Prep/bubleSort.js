function bubbleSort(arr) {
    // The length of the array
    const n = arr.length;
    // Variable to keep track if any swaps occurred in a pass
    let swapped;
    // Step 2: Start a do-while loop, which continues until no swaps are made in a pass
    do {
        swapped = false; // Initialize swapped to false at the beginning of each pass
        // Step 3: Start a for loop to iterate through the array
        for (let i = 0; i < n - 1; i++) {
            // Step 4: Compare adjacent elements and swap if needed
            if (arr[i] > arr[i + 1]) {
                [arr[i], arr[i + 1]] = [arr[i + 1], arr[i]]; // Swap the elements
                swapped = true; // Set swapped to true since a swap occurred
            }
        }
        // Step 5: Check if any swaps were made in the current pass. If not, the array is sorted.
    } while (swapped);

    // Step 6: Return the sorted array
    return arr;
}

// Example usage:
const unsortedArray = [64, 34, 25, 12, 22, 11, 90];
const sortedArray = bubbleSort(unsortedArray);
console.log(sortedArray); // Output: [11, 12, 22, 25, 34, 64, 90]
