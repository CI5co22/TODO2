$(document).ready(function() {
    $('.p-1').each(function() {
        let prioridad = $(this).data('prioridad'); 
        
        $(this).removeClass('p1 p2 p3');

        if(prioridad == 'Alta') {
            $(this).addClass('p1');
        } else if(prioridad == 'Media') {
            $(this).addClass('p2');
        } else if(prioridad == 'Baja') {
            $(this).addClass('p3');
        }
    });
});
