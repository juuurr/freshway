// Call the dataTables jQuery plugin
$(document).ready(function() {
  $('#dataTable').DataTable();
});


// Ensure PapaParse is loaded before this script
// Call the dataTables jQuery plugin

// $(document).ready(function() {
//   // Fetch the CSV data
//   fetch('data/menu.csv')
//       .then(response => response.text())
//       .then(csvData => {
//           Papa.parse(csvData, {
//               header: true,
//               dynamicTyping: true,
//               complete: function(results) {
//                   const data = results.data;
//                   const tableBody = $('#dataTable tbody');
//                   tableBody.empty();  // Clear existing rows

//                   // Populate table with CSV data
//                   data.forEach(row => {
//                       const tr = $('<tr></tr>');
//                       Object.values(row).forEach(cellValue => {
//                           const td = $('<td></td>').text(cellValue);
//                           tr.append(td);
//                       });
//                       tableBody.append(tr);
//                   });

//                   // Initialize DataTable after loading data
//                   $('#dataTable').DataTable();
//               }
//           });
//       })
//       .catch(error => console.error("Error fetching or parsing the CSV:", error));
// });