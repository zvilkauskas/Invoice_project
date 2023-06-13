$(".product-list-table").hide();

$(document).ready(function () {

    $(document).on('change keyup', '.quantity', function () {
        var quantity = $(this).attr('id')
        var priceId = '#' + $(this).attr("id").replace("quantity", "price");
        var price = $(priceId).text();
        var sum = '#' + $(this).attr("id").replace("quantity", "sum");
        var newPrice = parseFloat(price) * parseFloat($(this).val());
        $(sum).text(newPrice);
    });

    $(document).on('click', '.delete', function () {
        var row = $(this).data('row');
        $(this).closest('tr').remove();
    });

    $('#select-box2').on('change', function () {
        $(".product-list-table").show();
        let id = $(this).find(":selected").val();

        $("#product-table").find('tbody')
            .append($('<tr>')
                .append($('<td>')
                    .append($('<p>')
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
                        .text('0').attr('id', 'sum' + id).attr('name', 'sum')
                    )
                )
                .append($('<td>')
                    .append($('<a class="delete btn btn-danger" data-row="' + id + '">Trinti</a>'))
                )
            );
    });
});