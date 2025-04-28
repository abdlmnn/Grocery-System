const stock = document.getElementById('stockChart');
const subcat = document.getElementById('subcategoryChart');

const chart1 = {
    type: 'line',
    data: {
        labels: window.chartData.labels,
        datasets: [{
            label: 'Stock Quantity',
            data: window.chartData.data,
            backgroundColor: 'rgba(241, 123, 13, 0.2)',
            borderColor: '#f17b0d',
            borderWidth: 1,
            tension: 0.3,
            fill: true,
            pointBackgroundColor: '#f17b0d', 
            pointRadius: 3,
            pointHoverRadius: 6,
        }]
    },
    options: {
        responsive: true,
        maintainAspectRatio: false,
        scales: {
            x: {
                grid: {
                    color: 'rgba(147, 146, 144, 0.2)' 
                },
                ticks: {
                    font: {
                        size: 10,
                        // weight: 'bold'
                    }
                }
            },
            y: {
                beginAtZero: true,
                grid: { 
                    color: 'rgba(147, 146, 144, 0.2)' 
                },
                ticks: {
                    font: {
                        size: 10,
                        // weight: 'bold'
                    }
                }
            }
        }
    },
}


const chart2 = {
    type: 'line',
    data: {
        labels: window.chartData.labels2,
        datasets: [{
            label: 'Total Stock Quantity',
            data: window.chartData.data2,
            backgroundColor: 'rgba(241, 123, 13, 0.2)',
            borderColor: '#f17b0d',
            borderWidth: 1,
            tension: 0.3,
            fill: true,
            pointBackgroundColor: '#f17b0d', 
            pointRadius: 3,
            pointHoverRadius: 6,
        }]
    },
    options: {
        responsive: true,
        maintainAspectRatio: false,
        scales: {
            x: {
                grid: {
                    color: 'rgba(147, 146, 144, 0.2)' 
                },
                ticks: {
                    font: {
                        size: 10,
                        // weight: 'bold'
                    }
                }
            },
            y: {
                beginAtZero: true,
                grid: { 
                    color: 'rgba(147, 146, 144, 0.2)' 
                },
                ticks: {
                    font: {
                        size: 10,
                        // weight: 'bold'
                    }
                }
            }
        }
    }
};


new Chart(stock,chart1);
new Chart(subcat,chart2);