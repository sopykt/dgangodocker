new VenoBox({
    selector: '.venobox',
    numeration: true,
    infinigall: true,
    share: true,
    spinner: 'grid'
});
jQuery(document).ready(function($) {
    $(".clickable-row").click(function() {
        window.location = $(this).data("href");
    });
});