// Validar mail
function validarEmail(email) {
    expr = /^([a-zA-Z0-9_\.\-])+\@(([a-zA-Z0-9\-])+\.)+([a-zA-Z0-9]{2,4})+$/;
    if ( !expr.test(email) )
        alert("Error: La dirección de correo " + email + " es incorrecta.");
        return false;
}
// Cifrado SHA
function cifrar(){
        var input_pass = document.getElementById("clave");

        input_pass.value = SHA1(input_pass.value);		
    }
function cifrar2(){
    var input_pass = document.getElementById("clave2");

    input_pass.value = SHA1(input_pass.value);		
}
