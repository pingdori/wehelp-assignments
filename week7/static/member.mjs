import fetch from 'node-fetch'
async function get_data(username){
    let conn = await fetch("http://127.0.0.1:3000/api/members?username="+username);
    let conn_data = await conn.json();
    console.log(conn_data);
    let content=document.getElementById("result");
    content.innerHTML=this.responseText
}


