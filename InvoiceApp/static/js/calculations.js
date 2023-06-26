$(".product-list-table").hide();

$(document).ready(function () {

    $(document).on('change keyup', '.product_quantity', function () {
        var quantity = $(this).attr('id')
        var priceId = '#' + $(this).attr("id").replace("product_quantity", "product_price");
        var price = $(priceId).text();
        var sum = '#' + $(this).attr("id").replace("product_quantity", "product_sum");
        var newPrice = parseFloat(price) * parseFloat($(this).val());
        $(sum).text(newPrice);
        calculateTotal()
        getData()
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
                    .append($('<input type="text" class="product_quantity">')
                        .text('0').attr('id', 'product_quantity' + id)
                    )
                )
                .append($('<td>')
                    .append($('<p>')
                        .text($(this).find(":selected").data('price')).attr('id', 'product_price'+id).attr('class', 'product_price')
                    )
                )
                .append($('<td>')
                    .append($('<p class="product_sum">')
                        .text('0').attr('id', 'product_sum' + id)
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
        getData()
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
                        .text($(this).find(":selected").data('price')).attr('id', 'service_price'+id).attr('class', 'service_price')
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

    $('.product_sum, .service_sum').each(function() {
        var value = parseFloat($(this).text());

        if (!isNaN(value)) {
            sum += value;
        }
    });

    $('.totalSum').val(sum.toFixed(2));
}

function getData() {
    var objects = [];

    $('#product-table tbody tr').each(function() {
        var rowData = {};

        var name = $(this).find('.product_name').text();
        var quantity = $(this).find('.product_quantity').val();
        var total = $(this).find('.product_sum').text();
        var price = $(this).find('.product_price').text();

        rowData.type = 'product';
        rowData.name = name;
        rowData.quantity = quantity;
        rowData.price = price;
        rowData.total = total;

        objects.push(rowData);
    });

    $('#service-table tbody tr').each(function() {
        var rowData = {};

        var name = $(this).find('.service_name').text();
        var quantity = $(this).find('.service_quantity').val();
        var total = $(this).find('.service_sum').text();
        var price = $(this).find('.service_price').text();

        rowData.type = 'service';
        rowData.name = name;
        rowData.quantity = quantity;
        rowData.price = price;
        rowData.total = total;

        objects.push(rowData);
    });
    var jsonified_objects = JSON.stringify(objects);
//    console.log(objects);
//    console.log(jsonified_objects)
    $('.invoiceProductsServices').val(jsonified_objects);
}



