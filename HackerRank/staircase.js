// Consider a staircase of size :

//    #
//   ##
//  ###
// ####
// Observe that its base and height are both equal to , and the image is drawn using # symbols and spaces. The last line is not preceded by any spaces.

// Write a program that prints a staircase of size .

// Function Description

// Complete the staircase function in the editor below. It should print a staircase as described above.

// staircase has the following parameter(s):

// n: an integer
// Input Format

// A single integer, , denoting the size of the staircase.

// Constraints

//  .

// Output Format

// Print a staircase of size  using # symbols and spaces.

// Note: The last line must have  spaces in it.

// Sample Input

// 6 
// Sample Output

//      #
//     ##
//    ###
//   ####
//  #####
// ######
// Explanation

// The staircase is right-aligned, composed of # symbols and spaces, and has a height and width of .

function staircase(n) {
    let string = ""
    for (let i = 0; i < n; i++) {
        for (let j = n; j > 0; j--) {
            if (j > i + 1) {
                string += " "
            } else {
                string += "#"
            }
        }
        string += "\n"
    }
    console.log(string)
}


function staircaseRecursion (numOfRows, hashtags="", numOfSpaces=0, spaces="", staircase="") {
    if ( numOfRows === 0) {
        return ""
    } else {
        for ( let s = 0; s < numOfSpaces; s++) {
            spaces += " "
        }
        numOfSpaces += 1
        for ( let h = 0; h < numOfRows; h++ ) {
            hashtags +=  "#"
        }
        staircase = staircaseRecursion(numOfRows - 1, "", numOfSpaces) + spaces + hashtags
    }
    return staircase + "\n"
}

//staircase(6)
console.log(staircaseRecursion(6))