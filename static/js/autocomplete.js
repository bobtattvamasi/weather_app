// autocomplete.js
$(function() {
    $("#city").autocomplete({
        source: function(request, response) {
            $.ajax({
                url: "/autocomplete",
                data: { q: request.term },
                success: function(data) {
                    console.log("Received data:", data); // Debugging line
                    response(data);
                },
                error: function(xhr, status, error) {
                    console.error("Autocomplete error:", status, error);
                }
            });
        },
        minLength: 2,
    });
});
