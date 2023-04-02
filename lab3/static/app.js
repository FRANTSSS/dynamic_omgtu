
function create_request(){
    var httpRequest;
    if (window.XMLHttpRequest) {
        httpRequest = new XMLHttpRequest();
    }
    else if (window.ActiveXObject) {
        httpRequest = new ActiveXObject("Microsoft.XMLHTTP");
    }
    return httpRequest
}

function get_body_equation_roots(){
    var a = Number(document.getElementById("a_input").value);
    var b = Number(document.getElementById("b_input").value);
    var c = Number(document.getElementById("c_input").value);
    return JSON.stringify({
        "a": a,
        "b": b,
        "c": c
    })
}

function alert_result_roots(roots_list){
    if (roots_list.length == 1){
        document.getElementById("result__x1").textContent = `${roots_list[0]['name']}: ${roots_list[0]['value']}\n`
    }
    else if (roots_list.length == 2){
        document.getElementById("result__x1").textContent = `${roots_list[0]['name']}: ${roots_list[0]['value']}\n`
        document.getElementById("result__x2").textContent = `${roots_list[1]['name']}: ${roots_list[1]['value']}\n`
    }
}


function clear_alert_roots(){
    document.getElementById("result__x1").textContent = ""
    document.getElementById("result__x2").textContent = ""
    document.getElementById("error-msg").textContent = ""
}


function view_result(httpRequest){
    if (httpRequest.readyState == 4){
        clear_alert_roots()

        result = JSON.parse(httpRequest.responseText)
        if (result["message"] != null){
            document.getElementById("error-msg").textContent = result["message"]
        }
        else{
            alert_result_roots(result["data"])
        }
    }
}

function send_roots_equation(){
    var httpRequest = create_request()
    httpRequest.onreadystatechange = function() { view_result(httpRequest); };
    httpRequest.open("POST", "http://0.0.0.0:8000/equation/roots", true);
    httpRequest.setRequestHeader("Content-Type", "application/json;charset=utf-8")
    httpRequest.send(get_body_equation_roots());
}

solve_roots__btn.addEventListener("click", send_roots_equation);
