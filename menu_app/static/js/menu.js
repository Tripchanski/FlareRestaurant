let buttonsPlus = document.querySelectorAll('.button-plus');
let buttonsMinus = document.querySelectorAll('.button-minus');
let counters = document.querySelectorAll('.counter');

buttonsPlus.forEach(function(button) {
    button.addEventListener('click', function() {
        let counter = this.parentNode.querySelector('.counter');
        let defaultValue = parseInt(counter.value);
        if (defaultValue < 10) {
            let newValue = defaultValue + 1;
            counter.value = newValue;
            console.log(counter.value);
        }
    });
});

buttonsMinus.forEach(function(button) {
    button.addEventListener('click', function() {
        let counter = this.parentNode.querySelector('.counter');
        let defaultValue = parseInt(counter.value);
        if (defaultValue > 1) {
            let newValue = defaultValue - 1;
            counter.value = newValue;
            console.log(counter.value);
        }
    });
});



$('.add-to-cart-form').submit(function(e) {
    e.preventDefault();
    let data = $(this).serializeArray();
    let form = $(this);
    console.log(form);
    $.ajax({
        type: 'POST',
        url: form.find('.product').val(),
        data: data,
        success: function(response) {
            console.log(111)
            if (response.is_in_cart) {
                let cartCounter = $('.cart-counter');
                let newCartCounterValue = parseInt(cartCounter.text()) + 1;
                cartCounter.text(newCartCounterValue);
            } else {
                let cartCounter = $('.cart-counter');
                cartCounter.text(newCartCounterValue);
            }
        } 
    });
});
