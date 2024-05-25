document.addEventListener('DOMContentLoaded', function () {
    var tableModal = document.getElementById('tableModal');
    var addTableModal = document.getElementById('addTableModal');
    var tableDetails = document.getElementById('tableDetails');
    var closeButtons = document.querySelectorAll('.close');
    var openAddTableModalBtn = document.getElementById('openAddTableModal');

    // Open table details modal when table item is clicked
    document.querySelectorAll('.table-item').forEach(function(item) {
        item.addEventListener('click', function(event) {
            if (!event.target.classList.contains('delete-btn')) {
                var tableName = this.getAttribute('data-table-name');
                var databaseName = this.getAttribute('data-database-name');
                var description = this.getAttribute('data-description');
                tableDetails.innerHTML = `<strong>Table Name:</strong> ${tableName}<br><strong>Database Name:</strong> ${databaseName}<br><strong>Description:</strong> ${description}`;
                tableModal.style.display = 'block';
            }
        });
    });

    // Handle delete button click
    document.querySelectorAll('.delete-btn').forEach(function(button) {
        button.addEventListener('click', function(event) {
            event.stopPropagation(); // Prevent triggering the table item click event
            var tableName = this.getAttribute('data-table-name');
            if (confirm(`Are you sure you want to delete the table '${tableName}'?`)) {
                fetch(`/delete_table`, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({ table_name: tableName })
                }).then(response => {
                    if (response.ok) {
                        location.reload();
                    } else {
                        alert('Failed to delete table');
                    }
                });
            }
        });
    });

    // Close modals when the close button is clicked
    closeButtons.forEach(function(btn) {
        btn.onclick = function () {
            this.closest('.modal').style.display = 'none';
        };
    });

    // Close modals when clicking outside the modal content
    window.onclick = function (event) {
        if (event.target == tableModal) {
            tableModal.style.display = 'none';
        } else if (event.target == addTableModal) {
            addTableModal.style.display = 'none';
        }
    }

    // Open add table modal when the button is clicked
    openAddTableModalBtn.onclick = function () {
        addTableModal.style.display = 'block';
    }
});
