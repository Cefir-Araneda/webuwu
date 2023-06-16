var nombre = document.getElementById('mecanico');
var modelo = document.getElementById('modelo');
var patente = document.getElementById('patente');
var diagnostico = document.getElementById('diagnostico');
var cantidad = document.getElementById('cantidad');
var valor = document.getElementById('valor');
var error = document.getElementById('error');

function enviarFormulario() {
    console.log('Enviando formulario...');
    var mensajesError = [];
    let valorInt = parseInt(valor.value);

    if(nombre.value === null || nombre.value === '') {
        mensajesError.push('Ingresa nombre')
    }
    
    if(modelo.value === null || nombre.value === '') {
        mensajesError.push('Ingresa un modelo')
    }
    if(patente.value === null || patente.value === '' || patente.value.length !=6) {
        mensajesError.push('Ingresa patente correcta')
    }
    if(diagnostico.value === null || diagnostico.value === '' || diagnostico.value.length < 20) {
        mensajesError.push('Ingresa un diagnostico valido')
    }
    if(cantidad.value === null || cantidad.value === '') {
        mensajesError.push('Ingresa el numeor de mantenciones')
    }
    if(valor.value === null || valor.value === '' ||!Number.isInteger(valorInt)) {
        mensajesError.push('Ingresa el valor total')
    }

    error.innerHTML = mensajesError.join(', ');

    return false;
}