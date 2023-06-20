function deleteCompany(company_id) {
    var first_confirm = confirm('Ar tikrai norite ištrinti savo įmonės rekvizitus?');
    if (first_confirm && company_id) {
        var second_confirm = prompt("Patvirtinkite ištrynimą įrašydami žodį 'taip' :");
        if (second_confirm === 'taip') {
            $.ajax({
                headers: { "X-CSRFToken": csrfToken },
                method:'POST',
                url: 'ajax_delete_company/',
                data: {
                    company_id: company_id,
                },
                success: function (confirmation) {
                    //window.location.href = confirmation.redirect;
                        //return alert(confirmation.message);
                    alert(confirmation.message);
                    return window.location.href = confirmation.redirect;
                }
            });
        } else {
            return false;
        }
    } else {
        return false;
    }
}