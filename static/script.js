document.addEventListener('DOMContentLoaded', function () {
    var tableModal = document.getElementById('tableModal');
    var addTableModal = document.getElementById('addTableModal');
    var tableDetails = document.getElementById('tableDetails');
    var tableSpan = document.getElementsByClassName('close')[0];
    var addTableSpan = document.getElementsByClassName('close')[1];
    var openAddTableModalBtn = document.getElementById('openAddTableModal');
//    var closeButtons = document.querySelectorAll('.close');


    document.querySelectorAll('.table-item').forEach(function(item) {
        item.addEventListener('click', function() {
            var tableName = this.getAttribute('data-table-name');
            tableDetails.textContent = 'Details for table: ' + tableName;
            tableModal.style.display = 'block';
        });
    });

    // Close modals when the close button is clicked
//    closeButtons.forEach(function(btn) {
//        btn.onclick = function () {
//            this.closest('.modal').style.display = 'none';
//        };
//    });

    tableSpan.onclick = function () {
        tableModal.style.display = 'none';
    }

    addTableSpan.onclick = function () {
        addTableModal.style.display = 'none';
    }

    window.onclick = function (event) {
        if (event.target == tableModal) {
            tableModal.style.display = 'none';
        } else if (event.target == addTableModal) {
            addTableModal.style.display = 'none';
        }
    }

    openAddTableModalBtn.onclick = function () {
        addTableModal.style.display = 'block';
    }
});
