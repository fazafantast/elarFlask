function showTable() {
    let countRows = document.getElementById('count-rows').value;
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open( "GET", `/show-table/${countRows}/`, false );
    xmlHttp.send( null );
    let response = xmlHttp.responseText;
    document.getElementById('result-response').innerHTML = response;
}