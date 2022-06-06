{/* <table>
 <thead>
  <tr>
   <td> ... </td>
  </tr>
 </thead>
 <tfoot> ... </tfoot>
 <tbody> ... </tbody>
</table> */}


class uRow
{
    row=document.createElement("tr");
    // node=[];
    constructor(_id, list=[])
    {
        let c=document.getElementById(_id);
        this.row.id=_id;
        for (let i = 0; i < list.length; i++) 
        {
            let col=document.createElement("td");
            let text=document.createTextNode(list[i]);
            this.row.appendChild(col);
            col.appendChild(text); 
            // this.node.push(col);
            
        }
        c.replaceWith(this.row);
    }
    
}




class utable{

    JSONdata;
    table=document.createElement("table");
    thead=document.createElement("thead");
    tbody=document.createElement("tbody");
    tfoot=document.createElement("tfoot");

    constructor(_id)
    {
        let c=document.getElementById(_id);
        this.table.setAttribute("class","table");
        this.table.appendChild(this.thead);
        this.table.appendChild(this.tbody);
        this.table.appendChild(this.tfoot);
        c.replaceWith(this.table);
    }

    appendRow(name, array){
        let div=document.createElement("div");
        this.tbody.appendChild(div);
        div.id=name;
        // let r=
        new uRow(name,array);
    }

}





function sayHi(id) 
{
    let request = new XMLHttpRequest();  
    request.responseType = 'json';
    // request.responseType = 'text'; // now we're getting a string!
    
    request.onreadystatechange = function()
    {
            if (request.readyState == 4 && request.status == 200)
            {
                // alert("ok");                
                var json = request.response;
            }
    }
    request.onload = function() {
        // document.getElementById("output").innerHTML=request.response;
        var json = request.response;
        let a=new utable("output");
        for (var key in json){
            var value = json[key];
            
            a.appendRow(key,value);
          }
        
      }

    request.open("GET", "/params.json");
    request.send();
}


