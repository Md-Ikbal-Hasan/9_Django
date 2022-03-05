
document.addEventListener("DOMContentLoaded",function(event){

console.log("This is blog.js");
let sc = document.createElement('script')
sc.setAttribute('src' , 'https://cdn.tiny.cloud/1/no-api-key/tinymce/5/tinymce.min.js');

document.head.appendChild(sc);
sc.onload = ()=>
{

    tinymce.init({
        selector: '#id_content',
        width: 600,
        height: 300,
        plugins: [
            'advlist autolink link image lists charmap print preview hr anchor pagebreak',
            'searchreplace wordcount visualblocks visualchars code fullscreen insertdatetime media nonbreaking',
            'table emoticons template paste help'
        ],
        toolbar: 'undo redo | styleselect | bold italic | alignleft aligncenter alignright alignjustify | ' +
            'bullist numlist outdent indent | link image | print preview media fullpage | ' +
            'forecolor backcolor emoticons | help',
        menu: {
            favs: { title: 'My Favorites', items: 'code visualaid | searchreplace | emoticons' }
        },
        menubar: 'favs file edit view insert format tools table help',
        content_css: 'css/content.css'
    });
    



}



});