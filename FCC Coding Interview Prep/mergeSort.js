function mergeSort(arr){
    if (arr.length <= 1) {
        return arr;
    }
    const mid = Math.floor(arr.length/2);
    const leftArr = arr.slice(0, mid);
    const rightArr = arr.slice(mid);

    return merge(mergeSort(leftArr), mergeSort(rightArr));
}

function merge(leftArr, rightArr){
    const result = [];
    while(leftArr.length && rightArr.length){
        if (leftArr[0] < rightArr[0]){
            result.push(leftArr.shift());
        } else {
            result.push(rightArr.shift());
        }
    }
    return [...result, ...leftArr, ...rightArr];
}

//example
const unsortedArray = [64, 34, 25, 12, 22, 11, 90];
const sortedArray = mergeSort(unsortedArray);
console.log(sortedArray); // Output: [11, 12, 22, 25, 34, 64, 90]