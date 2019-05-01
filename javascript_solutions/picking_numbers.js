function pickSubArray(num1, num2, a) {
    let subArray = [];
    for (let i = 0; i < a.length; i++) {
        if (a[i] == num1 || a[i] == num2) {
            subArray.push(a[i]);
        }
    }
    return subArray;
}

function presentIn(num, a) {
    for (let i = 0; i < a.length; i++) {
        if (num == a[i]) {
            return true;
        }
    }
    return false;
}

function pickingNumbers(a) {
    // Write your code here
    let maxSize = 0
    let eliminated = [];
    while (a.length > 0) {
        let current = a[0];
        let smaller = a[0] - 1;
        let smallerSubArray = [];
        if (smaller >= 0 && !presentIn(smaller, eliminated)) {
            smallerSubArray = pickSubArray(current, smaller, a)
        }
        let smallSize = smallerSubArray.length;
        let bigger = a[0] + 1;
        let biggerSubArray = [];
        if (bigger <= 100 && !presentIn(bigger, eliminated)) {
            biggerSubArray = pickSubArray(current, bigger, a)
        }
        let bigSize = biggerSubArray.length;
        let largerSize = smallSize >= bigSize ? smallSize : bigSize;
        maxSize = largerSize > maxSize ? largerSize : maxSize
        console.log(smaller, a, bigger);
        console.log(smallerSubArray, biggerSubArray, maxSize);
        console.log('------')
        eliminated.push(current);
        a = a.filter(num => num != current);
    }
    return maxSize;
}