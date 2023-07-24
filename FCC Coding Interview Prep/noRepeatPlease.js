// Return the number of total permutations of the provided string that don't have repeated 
//consecutive letters. Assume that all characters in the provided string are each unique.
// For example, aab should return 2 because it has 
//6 total permutations (aab, aab, aba, aba, baa, baa), 
//but only 2 of them (aba and aba) don't have the same letter (in this case a) repeating.


function permutations(str) {
    if (str.length === 1) {
      return [str];
    }
    let allPerms = [];
    for (let i = 0; i < str.length; i++) {
      const firstChar = str[i];
      const remainingChars = str.slice(0, i) + str.slice(i + 1);
      const permOfRemaining = permutations(remainingChars);
      for (const perm of permOfRemaining) {
        allPerms.push(firstChar + perm);
      }
    }
    return allPerms;
  }
  
  function hasConsecutiveRepeating(str) {
    for (let i = 0; i < str.length - 1; i++) {
      if (str[i] === str[i + 1]) {
        return true;
      }
    }
    return false;
  }
  
  function permAlone(str) {
    let notDuplicateItem = [];
    let perms = permutations(str);
    for (const perm of perms) {
      if (!hasConsecutiveRepeating(perm)) {
        notDuplicateItem.push(perm);
      }
    }
    return notDuplicateItem.length;
  }
  
  console.log(permAlone("aab")); // Output: 2
  console.log(permAlone("aaa")); // Output: 0
  console.log(permAlone("aabb")); // Output: 8
  console.log(permAlone("abcdefa")); // Output: 3600
  console.log(permAlone("abfdefa")); // Output: 2640
  console.log(permAlone("zzzzzzzz")); // Output: 0
  console.log(permAlone("a")); // Output: 1
  console.log(permAlone("aaab")); // Output: 0
  console.log(permAlone("aaabb")); // Output: 12
  