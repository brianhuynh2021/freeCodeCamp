/*Compare and update the inventory stored in a 2D array against a second 2D array of a fresh delivery. 
Update the current existing inventory item quantities (in arr1). If an item cannot be found, 
add the new item and quantity into the inventory array. 
The returned inventory array should be in alphabetical order by item.*/

/*updateInventory([
                    [21, "Bowling Ball"], 
                    [2, "Dirty Sock"], 
                    [1, "Hair Pin"], 
                    [5, "Microphone"]], 
                [
                    [2, "Hair Pin"], 
                    [3, "Half-Eaten Apple"], 
                    [67, "Bowling Ball"], 
                    [7, "Toothpaste"]]) 
 should return [
                [88, "Bowling Ball"], 
                [2, "Dirty Sock"], 
                [3, "Hair Pin"], 
                [3, "Half-Eaten Apple"], 
                [5, "Microphone"], 
                [7, "Toothpaste"]].*/
//write a function with above requirements
function updateInventory(arr1, arr2) {
    for (let i = 0; i < arr1.length; i++) {
      for (let j = 0; j < arr2.length; j++) {
        if (arr1[i][1] === arr2[j][1]) {
          arr1[i][0] += arr2[j][0];
          arr2.splice(j, 1);
        }
      }
    }
  
    // Add the remaining items from arr2 to arr1
    for (let i = 0; i < arr2.length; i++) {
      arr1.push(arr2[i]);
    }
  
    // Sort newArr alphabetically by item name
    for (let i = 0; i < arr1.length; i++) {
      for (let j = 0; j < arr1.length - i - 1; j++) {
        if (arr1[j][1] > arr1[j + 1][1]) {
          let temp = arr1[j];
          arr1[j] = arr1[j + 1];
          arr1[j + 1] = temp;
        }
      }
    }
  
    return arr1;
  }
  
  // Example inventory lists
  var curInv = [
      [21, "Bowling Ball"],
      [2, "Dirty Sock"],
      [1, "Hair Pin"],
      [5, "Microphone"]
  ];
  
  var newInv = [
      [2, "Hair Pin"],
      [3, "Half-Eaten Apple"],
      [67, "Bowling Ball"],
      [7, "Toothpaste"]
  ];
  

// Example inventory lists
var curInv = [
    [21, "Bowling Ball"],
    [2, "Dirty Sock"],
    [1, "Hair Pin"],
    [5, "Microphone"]
];

var newInv = [
    [2, "Hair Pin"],
    [3, "Half-Eaten Apple"],
    [67, "Bowling Ball"],
    [7, "Toothpaste"]
];

console.log(updateInventory(curInv, newInv));