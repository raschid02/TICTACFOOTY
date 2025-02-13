"use strict";
document.addEventListener("DOMContentLoaded", function() {
    const gridElement = document.getElementById("grid");

    function updateGrid(grid) {
        if (!gridElement) {
            console.error("Grid element not found");
            return;
        }
        gridElement.innerHTML = "";
        grid.forEach(function(row, rowIndex) {
            const rowDiv = document.createElement("div");
            rowDiv.classList.add("row");
            row.forEach(function(cell, cellIndex) {
                const cellButton = document.createElement("button");
                cellButton.classList.add("cell");
                cellButton.textContent = cell === " " ? "" : cell;
                cellButton.addEventListener("click", function() {
                    makeMove(rowIndex * 3 + cellIndex + 1);
                });
                rowDiv.appendChild(cellButton);
            });
            gridElement.appendChild(rowDiv);
        });
    }

    function makeMove(cell) {
        fetch("http://127.0.0.1:5000/make_move", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ cell: cell })
        })
        .then(function(response) { return response.json(); })
        .then(function(data) {
            if (data.error) {
                alert(data.error);
            } else {
                updateGrid(data.grid);
                if (data.winner) {
                    alert(data.winner + " hat gewonnen!");
                }
            }
        })
        .catch(function(error) {
            console.error("Fehler beim Senden des Zuges:", error);
        });
    }

    fetch("http://127.0.0.1:5000/get_grid")
        .then(function(response) { return response.json(); })
        .then(function(data) {
            updateGrid(data);
        })
        .catch(function(error) {
            console.error("Fehler beim Abrufen des Spielfelds:", error);
        });
});
