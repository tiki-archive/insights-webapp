<template>
  <span id="insightDisplay"> </span>
</template>

<script>
// import c3 from 'c3'

// const helper = require('./PieChart')
export default {
  data() {
    return {
      chart_data: null,
      URL: 'https://tiki-insights.s3.us-east-2.amazonaws.com/companies/amazon/most_frequent_subjects.json',
    }
  },
  activated() {
    this.$fetch()
  },
  async fetch() {
    console.log('fetch data')

    this.chart_data = await fetch(this.URL).then((res) => res.json())

    console.log('chart data')

    console.log(this.chart_data[0])

    const cols = []

    const data = this.chart_data.chart_data[0].data
    for (const i in data) {
      cols.push([data[i].key, data[i].value])
    }

    console.log(data)

    this.$c3.generate({
      bindto: '#insightDisplay',

      pie: {
        expand: false,
        label: {
          format: function (value, ratio, id) {
            return value
          },
        },
      },
      color: {
        pattern: [
          '#00B272',
          '#0036A0',
          '#003C1C',
          '#D11D62',
          '#FF763C',
          '#FFD225',
          '#C95822',
          '#D33A41',
        ],
      },
      data: {
        // iris data from R
        columns: cols,
        type: 'pie',
      },
    })
  },
  fetchOnServer: false,
  mounted() {},
}
</script>

<style scoped lang="sass">
@import "assets/styles/theme/default"

#insightDisplay
  align-self: center
  display: flex
  font-family: $font-family-nunito-sans
  font-weight: 400
  fill: white
  color: white
</style>
