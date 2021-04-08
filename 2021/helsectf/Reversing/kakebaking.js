const stekeovn = s => {
    const kutt = text => text.split('').map(c => c.charCodeAt(0));
    const fordoy = n => ("0" + Number(n).toString(16)).substr(-2);
    const krydre = krydder => kutt(s).reduce((a,b) => a ^ b, krydder);
    
    return s => s.split('')
        .map(kutt)
        .map(krydre)
        .map(fordoy)
        .join('');
}

var ingredienser = [
  "Eggeplomme",
  "Kardemomme",
  "Løk",
  "Salt",
  "Pepper",
  "Marsipan",
  "EGG{Napoleonskake}"
]

for(let i = 0; i < ingredienser.length; i++){
  var steke = stekeovn(ingredienser[i-1] ? ingredienser[i-1] : 'noSaltToday') 
  ingredienser[i] = steke(ingredienser[i])
 
}

console.log(ingredienser)
