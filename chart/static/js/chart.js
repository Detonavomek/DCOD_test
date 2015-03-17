/**
 * Created by torvald on 17/03/15.
 */
function changeClass() {
    $(this).prev().toggleClass('active')
}

function chart(region, countries) {
    $('#chart').highcharts({
        chart: {
            type: 'column'
        },
        title: {
            text: region
        },
        xAxis: {
            type: 'category',
            labels: {
                rotation: -45,
                style: {
                    fontSize: '13px',
                    fontFamily: 'Verdana, sans-serif'
                }
            }
        },
        yAxis: {
            min: 0,
            title: {
                text: 'Популяция (millions)'
            }
        },
        legend: {
            enabled: false
        },
        tooltip: {
            pointFormat: 'Популяция кроликов в 2015г: <b>{point.y:.1f} millions</b>'
        },
        series: [
            {
                name: region,
                data: countries,
                dataLabels: {
                    enabled: true,
                    rotation: -90,
                    color: '#FFFFFF',
                    align: 'right',
                    format: '{point.y:.1f}', // one decimal
                    y: 10, // 10 pixels down from the top
                    style: {
                        fontSize: '13px',
                        fontFamily: 'Verdana, sans-serif'
                    }
                }
            }
        ]
    });
}