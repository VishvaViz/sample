var a=3000
var b=200
var c=30
var least=0
if (a<b & a<c){
    least=a
}
else if(b<c & b<a){
    least=b
}
else if(c<a & c<b){
    least=c
}
console.log(least);