CKEDITOR.replace('content')

var editor = CKEDITOR.instances.editor;

// Define el ancho y la altura deseados
var nuevoAncho = '300px';
var nuevaAltura = '20px';

// Establece el nuevo tamaño
editor.resize(nuevoAncho, nuevaAltura);