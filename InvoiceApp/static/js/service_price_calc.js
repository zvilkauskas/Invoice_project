$(".service-list-table").hide();

$(document).ready(function(){

$(document).on('change keyup', '.service_quantity', function() {
        var quantity = $(this).attr('id')
        var priceId = '#'+ $(this).attr("id").replace("service_quantity", "service_price");
        var price = $(priceId).text();
        var sum = '#'+ $(this).attr("id").replace("service_quantity", "service_sum");
        var newPrice = parseFloat(price) * parseFloat($(this).val());
        $(sum).text(newPrice);
    });

    $('#select-box3').on('change', function(){
        $(".service-list-table").show();
        let id = $(this).find(":selected").val();

  $("#service-table").find('tbody')
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
    );
    });
});