var clave = document.getElementById('clave');
var mail = document.getElementById('mail');
var user = document.getElementById('user');
var clave2 = document.getElementById('clave2');
var mail2 = document.getElementById('mail2');
var error = document.getElementById('error');
var flag1 = true;
var flag2 = true;
var input_pass = document.getElementById("clave2");
// Validar mail
function validarEmail(email) {
    console.log('Enviando formulario...');
    expr = /^([a-zA-Z0-9_\.\-])+\@(([a-zA-Z0-9\-])+\.)+([a-zA-Z0-9]{2,4})+$/;
    if ( !expr.test(email) )
        alert("Error: La dirección de correo " + email + " es incorrecta.");
        return false;
}
function validarPass(clave) {
    if(clave2.value === null || clave2.value === '' || clave2.value.length < 7) {
        mensajesError.push('Ingresa una contraseña valida')
        clave2.value = '';
        flag1 = false;
    } else {
        clave2.value = SHA1(clave2.value);
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

function registro() {
    console.log('Enviando formulario...');
    var mensajesError = [];
    expr = /^([a-zA-Z0-9_\.\-])+\@(([a-zA-Z0-9\-])+\.)+([a-zA-Z0-9]{2,4})+$/;

    if(clave2.value === null || clave2.value === '' || clave2.value.length < 7) {
        mensajesError.push('Ingresa una contraseña valida')
        flag1 = false;
    } else {
        clave2.value = SHA1(clave2.value);
    }
    
    if (!expr.test(mail2.value)) {
        mensajesError.push('Dirección de correo incorrecta')
        clave2.value = '';
        flag2 = false;
    }
    if (!expr.test(user.value)) {
        mensajesError.push('Usuario de correo incorrecta')
        clave2.value = '';
        flag2 = false;
    }

    error.innerHTML = mensajesError.join('</br>');
    
    if (flag1 === true && flag2 === true) {
        return true;
    } else {
        return false;
    }
}
