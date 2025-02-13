document.addEventListener('DOMContentLoaded', () => {
    const element = document.getElementById('myElement');
    const gridElement = document.getElementById('grid');

    // Initialisiere das Spielfeld
    fetch('/get_grid')
        .then(response => response.json())
        .then(data => updateGrid(data));

    function updateGrid(grid) {
        gridElement.innerHTML = "";
        grid.forEach((row, rowIndex) => {
            const rowElement = document.createElement('div');
            rowElement.classList.add('row');
            row.forEach((cell, cellIndex) => {
                const cellElement = document.createElement('button');
                cellElement.classList.add('cell');
                cellElement.textContent = cell;
                cellElement.addEventListener('click', () => makeMove(rowIndex * 3 + cellIndex + 1));
                rowElement.appendChild(cellElement);
            });
            gridElement.appendChild(rowElement);
        });
    }

    function makeMove(cell) {
        fetch('/make_move', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ cell: cell })
        })
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                alert(data.error);
            } else {
                updateGrid(data.grid);
                if (data.winner) {
                    alert(data.winner + " hat gewonnen!");
                }
            }
        });
    }
});
