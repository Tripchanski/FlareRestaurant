$(document).ready(function () {
    $('.delete-from-cart').submit(function(e) {
        e.preventDefault();
        let data = $(this).serializeArray()
        let form = $(this)
        let receiptProduct = $('.solo-product-'+data[1].value)
        let totalPrice = parseInt($('.total-price').text());
        console.log(receiptProduct)
        console.log(totalPrice)
        console.log(data[1].value)
        // console.log(data)
        $.ajax({
            type: "POST",
            url: $('#url_delete_from_cart').val(),
            data: data,
            success: function(response){
                form.remove()
                receiptProduct.remove()
                $('.total-price').html(response.full_price)
                let cartCounter = $('.cart-counter');
                let newCartCounterValue = parseInt(cartCounter.text()) - 1;
                cartCounter.text(newCartCounterValue);
            }
        })
    })
    $('.submit-order').click(function(e) {
        e.preventDefault();
        $.ajax({
            type: 'POST',
            url: $('#success_order').val(),
            data: $(this).parent().serializeArray(),
            success: function() {
                $('.product_in_cart').remove();
                $('.receipt-text').remove();
                $('.total-price').html('0')
                $('.modal-overlay').css('display', 'none');
                let cartCounter = $('.cart-counter');
                cartCounter.text(0);
            }
        })
        
    })
})



$('.go-to-order').on('click', function() {
    $.get($("#cart_url").val(), function (data) {
        // Выбор контейнера на другой странице, куда будет отображено содержимое
        let container = $(".modal");
        // Вставка полученного HTML-содержимого в контейнер
        container.html(data);
      });
    $('.modal-overlay').css('display', 'flex');
})

$('.times-sign').on('click', function() {
    $('.modal-overlay').css('display', 'none');
})
// function updateFinalPrice() {
//     let total
// }