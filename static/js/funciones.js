
function muestra_modal(url, titulo){
    document.getElementById('formEliminar').action = url;
    document.getElementById('modal-cuerpo').innerHTML = `¿Deseas eliminar el videojuego ${titulo}?`;
}

$("#id_estado").on('change',function (e) { 
    alert('Hola');
    alert(this.value);
});