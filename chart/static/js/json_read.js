/**
 * Created by torvald on 17/03/15.
 */
$.get('/ajax/more_dogs/', function(data) {
    // data is the response data. In this case, our JSON
    // Our JSON contains several dictionaries for each breed of dog,
    // and we want to construct an HTML table row for each
    // First, lets get the table body which we'll add the rows to
    $tbody = $("#dog_table").find('tbody');
    // next, iterate through the JSON array
    $.each(data, function() {
        // create the row
        $row = $('<tr>');
        // iterate through each dog breed's attributes and create a column for each key, value pair
        $.each(this, function(key, value) {
            // create the column
            $col = $('<td>');
            // add text to the column
            $col.text(key+":"+value);
            // append the column to the row
            $row.append($col);
        }
        // append the row to the table body
        $tbody.append($row);
    }
});