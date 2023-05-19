function sortTable(n) {
  var table = document.getElementsByClassName("my-table")[0];
  if (!table) return;

  var rows = Array.from(table.rows);
  var sortedRows = rows.slice(1).sort(function(a, b) {
    var x = a.cells[n].textContent.toLowerCase();
    var y = b.cells[n].textContent.toLowerCase();
    if (isNaN(parseFloat(x)) || isNaN(parseFloat(y))) {
      return x.localeCompare(y);
    }
    return parseFloat(x) - parseFloat(y);
  });
  table.tBodies[0].append(...sortedRows);
}
