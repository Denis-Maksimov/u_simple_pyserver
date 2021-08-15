

function 
create_checker(id)
{
    let a=document.createElement("div");
    let b=document.createTextNode("Hello, div");
    let c=document.getElementById(id);
    
    a.appendChild(b);
    a.id=id;
    a.onchange=function(){set_checker(this.id);}
    a.class="toggle-button";
    
    c.replaceWith(a);
    // c.replaceChild(a,c.children[0]);

    return a;
}


class checker{
    constructor(id)
    {
        let c=document.getElementById(id);
        this.div=document.createElement("div");
        this.chbox=document.createElement("input");
        // <label for="toggle-button" class="text">Toggle Button</label>

        this.label=document.createElement("label");
        this.text=document.createTextNode(id);
        c.replaceWith(this.div);

        this.chbox.type="checkbox";
        this.div.setAttribute("class", "container");
        this.label.setAttribute("class", "text");
        this.label.setAttribute("for", id);
        this.chbox.id=id;
        this.chbox.setAttribute("class", "toggle-button");
        this.chbox.onchange=function (ev) {
            respSetJSON();
        };

        this.div.appendChild(this.chbox);
        this.div.appendChild(this.label);
        this.label.appendChild(this.text);
        this.request = new XMLHttpRequest(); 
        this.request.onreadystatechange = function()
        {
                if (this.request.readyState == 4 && this.request.status == 200)
                {
                    // alert("ok");                
                    // var json = request.response;
                }
        }
        this.request.onload = function()
        {
        }
    }

    respSetJSON() 
    {
        this.request.responseType = 'json';
        this.request.open("POST", "/set_params");    
        this.request.send('{"'+this.id+'": ["'+String(this.chbox.checked)+'"]}');
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


function rap(){

    let chbox;
    chbox=document.getElementById('toggle-button');
    respSetJSON("chbox", String(chbox.checked));

};
function set_checker(id){

    let chbox;
    chbox=document.getElementById(id);
    respSetJSON(id, String(chbox.checked));

};

// document.onload.call()