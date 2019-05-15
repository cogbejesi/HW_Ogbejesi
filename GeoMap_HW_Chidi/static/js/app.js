// from data.js
var tableData = data;

// YOUR CODE HERE!
var tbody = d3.select("tbody");

function buildTable(data) {
    tbody.html("");

    // Next, loop through each and append a row and cell for each
    data.forEach((dataRow) => {
        // Append a row to the table body
        var row = tbody.append("tr");
    
        Object.values(dataRow).forEach((val) => {
          var cell = row.append("td");
            cell.text(val);
          }
        );
      });
    }

    function handleClick() {

        // Prevent the form from refreshing the page
        d3.event.preventDefault();
      
        // Grab the datetime value from the filter
        var date = d3.select("#datetime").property("value");
        let filteredData = tableData;

        if (date) {
            // Apply `filter` to the table data to only keep the
            // rows where the `datetime` value matches the filter value
            filteredData = filteredData.filter(row => row.datetime === date);
          }

          // Build the table using the filtered data

          buildTable(filteredData);
        }

        // Attach an event listener
        d3.selectAll("#filter-btn").on("click", handleClick);

        buildTable(tableData);
