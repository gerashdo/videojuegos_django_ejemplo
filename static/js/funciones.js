
function muestra_modal(url, titulo){
    document.getElementById('formEliminar').action = url;
    document.getElementById('modal-cuerpo').innerHTML = `¿Deseas eliminar el videojuego ${titulo}?`;
}