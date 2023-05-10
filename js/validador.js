var clave = document.getElementById('clave');
var mail = document.getElementById('mail');
var error = document.getElementById('error');
var flag1 = true;
var flag2 = true;
// Validar mail
function validarEmail(email) {
    console.log('Enviando formulario...');
    expr = /^([a-zA-Z0-9_\.\-])+\@(([a-zA-Z0-9\-])+\.)+([a-zA-Z0-9]{2,4})+$/;
    if ( !expr.test(email) ) {
        alert("Error: La dirección de correo " + email + " es incorrecta.");
        return false;
    } else {
        return true;
    }
}
function validarPass(clave) {
    if(clave.value === null || clave.value === '' || clave.value.length < 7) {
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

function acceder() {
    console.log('Enviando formulario...');
    var mensajesError = [];
    expr = /^([a-zA-Z0-9_\.\-])+\@(([a-zA-Z0-9\-])+\.)+([a-zA-Z0-9]{2,4})+$/;

    if(clave.value === null || clave.value === '' || clave.value.length < 7) {
        mensajesError.push('Ingresa una contraseña valida')
        flag1 = false;
    } else {
        clave.value = SHA1(clave.value);
    }
    
    if (!expr.test(mail.value)) {
        mensajesError.push('Dirección de correo incorrecta')
        clave.value = '';
        flag2 = false;
    }

    error.innerHTML = mensajesError.join('</br>');
    
    if (flag1 === true && flag2 === true) {
        return true;
    } else {
        return false;
    }
}
