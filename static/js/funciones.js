
function muestra_modal(url, titulo){
    document.getElementById('formEliminar').action = url;
    document.getElementById('modal-cuerpo').innerHTML = `¿Deseas eliminar el videojuego ${titulo}?`;
}

function muestra_modal_categoria(url, nombre){
    document.getElementById('formEliminar').action = url;
    document.getElementById('modal-cuerpo').innerHTML = `¿Deseas eliminar la categoria ${nombre}?`;
}

function muestra_modal_categoria(url, username){
    document.getElementById('formEliminar').action = url;
    document.getElementById('modal-cuerpo').innerHTML = `¿Deseas eliminar al usuario ${username}?`;
}


$("#id_estado").on('change', function() {
    var token = $('[name="csrfmiddlewaretoken"]').val();
    $.ajax({
        type: "post",
        url: `/usuarios/municipios/`,
        data: {'id':this.value,'csrfmiddlewaretoken':token},
        success: function (response) {
            var html = "";
            if (response[0].hasOwnProperty('error')){
                html+=`<option value="0">${response[0].error}</option>`;
            }else{
                $.each(response, function (llave, valor) { 
                    html+=`<option value="${valor.id}">${valor.nombre}</option>`;
               });
            }
            $("#id_municipio").html(html);
            // console.log(response);
        },
        error: function(param){
            console.log('Error en la peticion')
        }
    });
    // alert(this.value);
});