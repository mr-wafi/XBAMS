/* Chart 1 */



// chart 2
var ctx = document.getElementById("chart2").getContext('2d');
var myChart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: ['Sat', 'Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fr'],
        datasets: [{
            label: 'Admitted',
            data: [150, 200, 190, 190, 200, 230, 220],
            barPercentage: .5,
            backgroundColor: "#7366ff",


        }, {
            label: 'Discharge',
            data: [190, 140, 180, 240, 160, 190, 140],
            barPercentage: .5,
            backgroundColor: "#f73164",

        }]
    },
    options: {
        maintainAspectRatio: false,

        legend: {
            display: false,
            labels: {
                fontColor: '#585757',
                boxWidth: 40,

            }
        },
        tooltips: {
            enabled: true
        },
        scales: {
            xAxes: [{
                ticks: {
                    beginAtZero: true,
                    fontColor: '#585757'
                },
                gridLines: {
                    display: false,
                    color: "rgba(0, 0, 0, 0.07)"
                },
            }],
            yAxes: [{
                ticks: {
                    beginAtZero: true,
                    fontColor: '#585757'
                },
                gridLines: {
                    display: false,
                    color: "rgba(0, 0, 0, 0.07)"
                },
            }]
        }
    }
});


// chart 3
new Chart(document.getElementById("chart3"), {
    type: 'doughnut',
    data: {
        labels: ["Stroke", "Diabetes", "Cirrhosis", "Tuberculosis"],
        datasets: [{
            label: "Top Diseases (millions)",
            backgroundColor: ["rgba(115, 102, 255, 1)", "rgba(115, 102, 255, 0.8)", "rgba(115, 102, 255, 0.7)", "rgba(115, 102, 255, 0.6)"],
            // data: [2478, 5267, 734, 784],
            data: [1, 2, 1, 5]
        }]
    },
    options: {
        legend: {
            display: false,
            position: "left",

        },
        maintainAspectRatio: false,
        title: {
            display: false,
            text: 'Top Diseases'
        }
    }
});