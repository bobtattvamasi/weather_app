$(function() {
    $("#city").autocomplete({
        source: function(request, response) {
            $.ajax({
                url: "/autocomplete",
                data: { q: request.term },
                success: function(data) {
                    response(data);
                }
            });
        },
        minLength: 2,
    });
});
