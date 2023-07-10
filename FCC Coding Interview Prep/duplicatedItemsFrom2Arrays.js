//ex: Find out duplicated items of two arrays
// const arr1 = [1, 2, 3, 4, 5];
// const arr2 = [3, 4, 5, 6];

function duplicates2Arrays(arr1, arr2) {
  let duplicates = [];
  
  for (let i = 0; i < arr1.length; i++) {
    let found = false;
    
    for (let j = 0; j < arr2.length; j++) {
      if (arr1[i] === arr2[j]) {
        found = true;
        break;
      }
    }
    
    if (found && !duplicates.includes(arr1[i])) {
      duplicates.push(arr1[i]);
    }
  }
  
  return duplicates;
}

// Example usage
const arr1 = [1, 2, 3, 4, 5];
const arr2 = [3, 4, 5, 6];
const duplicates = duplicates2Arrays(arr1, arr2);
console.log(duplicates); // Output: [3, 4, 5]
