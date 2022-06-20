<template>
  <span id="insightDisplay"> </span>
</template>

<script>
// import c3 from 'c3'

const helper = require('./PieChart')
export default {
  data() {
    return {
      chart_data: null,
      URL: '<AMZ URL>',
    }
  },
  activated() {
    this.$fetch()
  },
  async fetch() {
    // this.chart_data = await fetch(this.URL).then((res) => res.json())
  },
  mounted() {
    const population = [
      { key: 'Test 2', value: 5 },
      { key: 'Test', value: 10 },
    ]

    this.chart_data = helper.PieChart(population, {
      name: (d) => d.key,
      value: (d) => d.value,
      width: 500,
      height: 500,
    })

    const el = document.getElementById('insightDisplay')

    while (el.hasChildNodes()) {
      el.removeChild(el.children[0])
    }

    el.appendChild(this.chart_data)
  },
}
</script>

<style scoped lang="sass">
@import "assets/styles/theme/default"

#insightDisplay
  align-self: center
  display: flex
</style>
