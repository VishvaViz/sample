let data=[
    {id:101,name:"susan",num:124},
    {id:102,name:"sara",num:1233},
    {id:103,name:"emily",num:1244},
    {id:104,name:"georgia",num:12422},
]

let s=data.filter((val)=>{
    if(val.hasOwnProperty("name")==true){
        // console.log(val.name);
        return val.name
    }
})

