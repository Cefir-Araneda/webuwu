var pass1 = document.getElementById('password1');
var pass2 = document.getElementById('password2');

if(pass1 != pass2) {
    var mensajesError = [];
    mensajesError.push("Las contraseñas ingresadas son distintas")
    return false
}