var clave = document.getElementById('clave');
// Validar mail
function validarEmail(email) {
    console.log('Enviando formulario...');
    expr = /^([a-zA-Z0-9_\.\-])+\@(([a-zA-Z0-9\-])+\.)+([a-zA-Z0-9]{2,4})+$/;
    if ( !expr.test(email) )
        alert("Error: La dirección de correo " + email + " es incorrecta.");
        return false;
}
function validarPass(clave) {
    if(clave.value === null || clave.value === '' || clave.value.length < 8) {
        mensajesError.push('Ingresa una contraseña valida')
    } else {
        clave.value = SHA1(clave.value);	
    }
}
function cifrar(){
        var input_pass = document.getElementById("clave");

        input_pass.value = SHA1(input_pass.value);		
    }
function cifrar2(){
    var input_pass = document.getElementById("clave2");

    input_pass.value = SHA1(input_pass.value);		
}
