document.addEventListener('DOMContentLoaded', function () {
    var modal = document.getElementById('tableModal');
    var span = document.getElementsByClassName('close')[0];
    var tableDetails = document.getElementById('tableDetails');

    document.querySelectorAll('.table-item').forEach(function(item) {
        item.addEventListener('click', function() {
            var tableName = this.getAttribute('data-table-name');
            tableDetails.textContent = 'Details for table: ' + tableName;
            modal.style.display = 'block';
        });
    });

    span.onclick = function () {
        modal.style.display = 'none';
    }

    window.onclick = function (event) {
        if (event.target == modal) {
            modal.style.display = 'none';
        }
    }
});
