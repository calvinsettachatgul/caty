arr = [1,2,2, 3,1,1,5, 4, 9];

// count the frequency of all the numbers in an array
// return a javascript object with keys as number and value as frequency

function countFrequency(arr){
    // create a map or 2d arrray maybe map would be better
    // iterate through the array
    // put the number and 1 in the map because it occured once
    let freqHash = {};
    for( var i = 0; i < arr.length; i++){
      let element = arr[i];  
      // the key value is already there
      if(freqHash[element]){
          freqHash[element]++
          
      // the key value is not there yet
      }else{
         freqHash[element] = 1; 
      }
    }
    return freqHash
};

console.log(countFrequency(arr))