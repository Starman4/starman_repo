import justpy as jp
import pandas
from datetime import datetime
from pytz import utc
import matplotlib.pyplot as plt

data=pandas.read_csv("reviews.csv",parse_dates=['Timestamp'])

data['Weekday']=data['Timestamp'].dt.strftime('%A')

weekday_average=data.groupby(['Weekday']).mean()
#plt.plot(weekday_average.index,weekday_average['Rating'])

#data =pandas.read_csv("reviews.csv",parse_dates=["Timestamp"])
#data['Month']=data['Timestamp'].dt.strftime('%Y-%m')
#month_average_crs=data.groupby(['Month','Course Name'])['Rating'].count().unstack()

chart_def="""{
    chart: {
        type: 'spline',
        inverted: false
    },
    title: {
        text: 'Average Rating by Week'
    },
    xAxis: {
        reversed: false,
        title: {
            enabled: true,
            text: 'Day'
        },
        labels: {
            format: '{value}'
        },
        accessibility: {
            rangeDescription: 'Range: 0 to 80 km.'
        },
        maxPadding: 0.05,
        showLastLabel: true
    },
    yAxis: {
        title: {
            text: 'Average Rating'
        },
        labels: {
            format: '{value}°'
        },
        accessibility: {
            rangeDescription: 'Range: -90°C to 20°C.'
        },
        lineWidth: 2
    },
    legend: {
        enabled: false
    },
    tooltip: {
        headerFormat: '<b>{series.name}</b><br/>',
        pointFormat: '{point.x}: {point.y}'
    },
    plotOptions: {
        spline: {
            marker: {
                enable: false
            }
        }
    },
    series: [{
        name: 'Average Rating',
        data: [[0, 15], [10, -50], [20, -56.5], [30, -46.5], [40, -22.1],
            [50, -2.5], [60, -27.7], [70, -55.7], [80, -76.5]]
    }]
}
"""

def app():
    wp=jp.QuasarPage()
    h1=jp.QDiv(a=wp, text="Analysis of Course Reviews",classes="text-h2 text-center q-pt-md")
    p1=jp.QDiv(a=wp, text="These graphs represent course review analysis")


    hc=jp.HighCharts(a=wp, options=chart_def)
    hc.options.xAxis.categories=list(weekday_average.index)
    hc.options.series[0].data=list(weekday_average['Rating'])
    #hc.options.xAxis.categories = list(weekly_average.index)
    #mean=[]
    #hc_data=[{"name":v1,"data":[4.455207,4.449335,4.440274,4.439097,4.437880,4.446240,4.427452]}]
    #hc_data=[{"name":v1,"data":[v2 for v2 in month_average_crs[v1]]} for v1 in month_average_crs.columns]
    #hc.options.series=hc_data
    return wp

jp.justpy(app)

