//Write a function for reversing numbers in binary. For instance, the binary representation of 13 is 1101, and reversing it gives 1011, which corresponds to number 11.

function reverseBinary(param) {
    return parseInt(param.toString(2).split("").reverse().join(""),2)
}
console.log(reverseBinary(18))
