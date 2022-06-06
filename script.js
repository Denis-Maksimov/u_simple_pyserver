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



