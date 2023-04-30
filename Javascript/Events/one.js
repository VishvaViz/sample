let details=[  {id:1,name:"Daisy",dept:"Bca"},
                {id:2,name:"Ben",dept:"Mca"},
                {id:3,name:"Susan",dept:"Bcom"},
                {id:4,name:"Clara",dept:"Bba"},
                {id:5,name:"Emma",dept:"Mba"}
            ]


let display_Data=()=>{
    let row="";
    for (data of details){
        row=row+`<tr>
                    <td>${data.id}</td>
                    <td>${data.name}</td>
                    <td>${data.dept}</td>
                </tr>
        `
    }
    
    document.getElementById("abc").innerHTML=row
}
display_Data()