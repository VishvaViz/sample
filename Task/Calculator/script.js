function display(input){
    document.getElementById("result").value+=input
}
function hello(){
    var output=eval(document.getElementById("result").value);
    document.getElementById("result").value=output;
}
function allclear(){
    document.getElementById("result").value=" ";
}
function del(){
    document.getElementById("result").value=result.value.slice(0,-1);
}
function color_Dark(){
    document.getElementById("dark").style.backgroundColor="rgba(0,0,0,0.5)"
    // d    ocument.getElementById("2").style.backgroundColor="rgba(0,0,0,0.5)"
}
function color_Light(){
    document.getElementById("dark").style.backgroundColor="#fff"
    document.getElementById("dark").style.color="black"
}
function normal(){
    document.getElementById("dark").style=""
}

