$('#gifModal').on('show.bs.modal', function (event) {
    var button = $(event.relatedTarget) // Button that triggered the modal
    var orig_url = button.data('origurl') // Extract info from data-* attributes
    var url_200 = button.attr('src')
    var img_id = button.data('imgid')
    $('#full_size').attr("src", orig_url)
    $('#img_200_url').attr("value", url_200)
    $('#img_orig_url').attr("value", orig_url)
    $('#img_id').attr("value", img_id)
})

$(function () {
    $('#submit-btn').on('click', function (e) {
        e.preventDefault();
        $.ajax({
            url: '/giphy/save/',
            data: $('#save-img-frm').serialize(),
            type: "POST",
            success: $('#gifModal').modal('toggle'),
            error: function () {
                alert('Something failed.')
            }
        });
        return false;
    });
});