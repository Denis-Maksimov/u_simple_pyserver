

function respSetJSON(parameter, value) 
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

    }

    request.open("POST", "/set_params");    
    request.send('{"'+parameter+'": ["'+value+'"]}');
}


class checker
{

    div=document.createElement("div");
    chbox=document.createElement("input");
    label=document.createElement("label");
    text;
    id;

    constructor(_id)
    {   
        this.id=_id;
        let c=document.getElementById(_id);
        this.text=document.createTextNode(_id);
        
        c.replaceWith(this.div);

            this.chbox.type="checkbox";
            this.chbox.id=_id;
            this.chbox.setAttribute("class", "toggle-button");
            this.chbox.setAttribute("onchange", "respSetJSON(this.id, this.checked);");
            
            this.div.setAttribute("class", "container");

            this.label.setAttribute("class", "text");
            this.label.setAttribute("for", _id);

        this.div.appendChild(this.chbox);
        this.div.appendChild(this.label);
        this.label.appendChild(this.text);     
        
    }

}



{/* <button class="custom-btn btn-11">
Кнопка 11
            <div class="dot"></div></button> */}
class ubutton
{

    div=document.createElement("div");
    btn=document.createElement("button");
    // label=document.createElement("label");
    text;
    id;

    constructor(_id)
    {   
        this.id=_id;
        let c=document.getElementById(_id);
        this.text=document.createTextNode(_id);
        
        c.replaceWith(this.div);

            // this.btn.type="button";
            this.btn.id=_id;
            this.btn.setAttribute("class", "custom-btn btn-11");
            this.btn.setAttribute("onclick", "respSetJSON(this.id, true);");
            
            this.div.setAttribute("class", "container");

            // this.label.setAttribute("class", "text");
            // this.label.setAttribute("for", _id);

        this.div.appendChild(this.btn);
        // this.div.appendChild(this.label);
        this.btn.appendChild(this.text);     
        
    }

}






function respJSON() 
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
      }

    request.open("GET", "/params.json");
    request.send();
}






// document.onload.call()