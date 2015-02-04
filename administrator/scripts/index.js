$( document ).ready(function() {
    $('#side-menu').metisMenu();
    $('#data-table').DataTable({
        responsive: true,
        retrieve: true,
    });
});