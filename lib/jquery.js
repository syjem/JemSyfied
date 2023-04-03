
$(function() {
    $('.home').on('click', function() {
        $('.about').removeClass('active');
        $('.gallery').removeClass('active');
        $('.contact').removeClass('active');
        $('.home').addClass('active');
    });

    $('.about').on('click', function() {
        $('.home').removeClass('active');
        $('.gallery').removeClass('active');
        $('.contact').removeClass('active');
        $('.about').addClass('active');
    });

    $('.gallery').on('click', function() {
        $('.home').removeClass('active');
        $('.about').removeClass('active');
        $('.contact').removeClass('active');
        $('.gallery').addClass('active');
    });

    $('.contact').on('click', function() {
        $('.home').removeClass('active');
        $('.about').removeClass('active');
        $('.gallery').removeClass('active');
        $('.contact').addClass('active');
    });
});