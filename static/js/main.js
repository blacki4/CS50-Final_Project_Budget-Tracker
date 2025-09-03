document.addEventListener("DOMContentLoaded", () => {
  // Expense Chart
  const expenseCtx = document.getElementById("expenseChart");
  if (expenseCtx) {
    fetch("/summary")
      .then((res) => res.json())
      .then((data) => {
        new Chart(expenseCtx, {
          type: "pie",
          data: {
            labels: Object.keys(data),
            datasets: [
              {
                label: "Expenses",
                data: Object.values(data),
                backgroundColor: [
                  "#FF6384",
                  "#36A2EB",
                  "#FFCE56",
                  "#4BC0C0",
                  "#9966FF",
                  "#FF9F40",
                ],
              },
            ],
          },
          options: { responsive: true },
        });
      });
  }

  // Income Chart
  const incomeCtx = document.getElementById("incomeChart");
  if (incomeCtx) {
    fetch("/income_summary")
      .then((res) => res.json())
      .then((data) => {
        new Chart(incomeCtx, {
          type: "pie",
          data: {
            labels: Object.keys(data),
            datasets: [
              {
                label: "Income",
                data: Object.values(data),
                backgroundColor: [
                  "#4BC0C0",
                  "#36A2EB",
                  "#FFCE56",
                  "#9966FF",
                  "#FF6384",
                  "#FF9F40",
                ],
              },
            ],
          },
          options: { responsive: true },
        });
      });
  }
});
