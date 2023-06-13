$(".product-list-table").hide();

$(document).ready(function () {

    $(document).on('change keyup', '.quantity', function () {
        var quantity = $(this).attr('id')
        var priceId = '#' + $(this).attr("id").replace("quantity", "price");
        var price = $(priceId).text();
        var sum = '#' + $(this).attr("id").replace("quantity", "sum");
        var newPrice = parseFloat(price) * parseFloat($(this).val());
        $(sum).text(newPrice);
        calculateTotal()
        getName()
    });


    $(document).on('click', '.delete', function () {
        var row = $(this).data('row');
        $(this).closest('tr').remove();
        calculateTotal()
    });


    $('#select-box2').on('change', function () {
        $(".product-list-table").show();
        let id = $(this).find(":selected").val();

        $("#product-table").find('tbody')
            .append($('<tr>')
                .append($('<td>')
                    .append($('<p class="product_name">')
                        .text($(this).find(":selected").data('name'))
                    )
                )
                .append($('<td>')
                    .append($('<p>')
                        .text($(this).find(":selected").data('description'))
                    )
                )
                .append($('<td>')
                    .append($('<input type="text" class="quantity">')
                        .text('0').attr('id', 'quantity' + id)
                    )
                )
                .append($('<td>')
                    .append($('<p>')
                        .text($(this).find(":selected").data('price')).attr('id', 'price' + id)
                    )
                )
                .append($('<td>')
                    .append($('<p class="sum">')
                        .text('0').attr('id', 'sum' + id)
                    )
                )
                .append($('<td>')
                    .append($('<a class="delete btn btn-danger" data-row="' + id + '">Trinti</a>'))
                )
            );
    });
});

$(".service-list-table").hide();

$(document).ready(function(){

    $(document).on('change keyup', '.service_quantity', function() {
        var quantity = $(this).attr('id')
        var priceId = '#'+ $(this).attr("id").replace("service_quantity", "service_price");
        var price = $(priceId).text();
        var sum = '#'+ $(this).attr("id").replace("service_quantity", "service_sum");
        var newPrice = parseFloat(price) * parseFloat($(this).val());
        $(sum).text(newPrice);
        calculateTotal()
        getName()
    });

    $(document).on('click', '.delete', function () {
        var row = $(this).data('row');
        $(this).closest('tr').remove();
        calculateTotal()
    });

    $('#select-box3').on('change', function(){
        $(".service-list-table").show();
        let id = $(this).find(":selected").val();

        $("#service-table").find('tbody')
            .append($('<tr>')
                .append($('<td>')
                    .append($('<p class="service_name">')
                        .text($(this).find(":selected").data('name'))
                    )
                )
                .append($('<td>')
                    .append($('<p>')
                        .text($(this).find(":selected").data('description'))
                    )
                )
                .append($('<td>')
                    .append($('<input type="text" class="service_quantity">')
                        .text('0').attr('id', 'service_quantity'+id)
                    )
                )
                .append($('<td>')
                    .append($('<p>')
                        .text($(this).find(":selected").data('price')).attr('id', 'service_price'+id)
                    )
                )
                .append($('<td>')
                    .append($('<p class="service_sum">')
                        .text('0').attr('id', 'service_sum'+id)
                    )
                )
                .append($('<td>')
                    .append($('<a class="delete btn btn-danger" data-row="' + id + '">Trinti</a>'))
                )
            );
    });
});

function calculateTotal() {
    var sum = 0;

    $('.sum, .service_sum').each(function() {
        var value = parseFloat($(this).text());

        if (!isNaN(value)) {
            sum += value;
        }
    });

    $('.totalSum').val(sum.toFixed(2));
}

function getName() {
    var objects = []
    $('.product_name, .service_name').each(function() {
       var value = $(this).text();
       objects.push(value);
    })

    $('.invoiceProducts').val(objects);
}



