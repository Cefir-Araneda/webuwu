// Validar mail
function validarEmail(email) {
    expr = /^([a-zA-Z0-9_\.\-])+\@(([a-zA-Z0-9\-])+\.)+([a-zA-Z0-9]{2,4})+$/;
    if ( !expr.test(email) )
        alert("Error: La dirección de correo " + email + " es incorrecta.");
        return false;
}
// Validar largo contraseña - cifrado access
function validarlargoa(par) {
    if ( par.length < 7 )
        alert("Error: Contraseña muy corta");

        var input_pass = document.getElementById("clave");

        input_pass.value = SHA1(input_pass.value);
        return false;
}
// Validar largo contraseña - cifrado register
function validarlargor(par) {
    if ( par.length < 7 )
        alert("Error: Contraseña muy corta");

        var input_pass = document.getElementById("clave2");

        input_pass.value = SHA1(input_pass.value);
        return false;
}
