$(document).ready(function() {
   
    $('.menu-item').hover(
        function() { // mouse enter
            $(this).find('.dropdown-menu').slideDown();
        },
        function() { // mouse leave
            $(this).find('.dropdown-menu').slideUp();
        }
    );

});
