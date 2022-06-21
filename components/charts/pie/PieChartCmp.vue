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
      URL: 'https://tiki-insights.s3.us-east-2.amazonaws.com/companies/amazon/most_frequent_subjects.json?response-content-disposition=inline&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBwaCXVzLWVhc3QtMiJGMEQCIAaWelJ9NjdCTJF5GMjc7G9tcnvau%2BWC8SkljWHgl%2Bi4AiBg%2BqXpbl%2BThMzJEh75bcnI6HAO4ZdOrRLfwwSwjJgplyr7Agg2EAEaDDE2NDQwODg2NDkyNyIMyGo%2ByDKJ%2FuXb7yZqKtgCf4But8Y9RQZ4eAu821ftBgeIC6QYH9O4n%2BsgMnFgm3Ek3nk0hFl4hWA1YRiF0wGF68SBvlZuj26J3eSByq4vd3QoKNuDCKrq%2FDdCudiF%2FsQyQnk1hEO%2BSVibdkrqSbVG4X31DQCi%2BFJ3RMni%2FpRf596gwjFMcKUor7TPBzgO46PIZA1WOPsU0WuIVYqNvBf2%2BWhlaWUB%2FysoZlb%2BZVoRMcQ%2FJYxoQ6Vkqem1pbdITFqgxlAcDmNbdyN2d0sVije6DLxj4vtSwHrSmMMAlwFvBjoLUz7peqig5ps3v%2Fye57jkvN%2FGp1VUlOc%2FNDy39j60oM3dxBU%2B9CvAf3nBB3cYvKSuelF7Acd6oV7Ev%2FihqcnCabBYKvIiqq9WZcXirltKZk8mubA%2BnHWLdGGYI4GMCtAXvXw5Gp1uY3%2FR7SiGJd59vI1eYlWEz5Hrgg6U4u8xG5hx%2Bonrc%2FAw5LDDlQY6tAJaHtalumMjQtC4LwgoQafVC14%2B5DqhGhwdX5CGq5TSEoG%2BjB8bGfXBqL3KDnh%2BTj58kHOYxJ2dpRpZYE8L%2B3KAIAMOUFAcqh%2B4diPZz8l1gFPHsCsdJndxytwPgV9WAmnbDMWkG0R2%2BQKsHFGLCWgZEm57VI8QZwAlioptgEUrDyXGLFasqg7nlYnAJ3ECd6LjIRwPsd85CEwIHvH%2Bv1XTeXXGvgwQxTFpgNCgLB2eCLg0YSfIRZAQV1GHbl5ohIHrCQVMfcH2Rklb59hzU7ApIVfk2v8UsOJxS07%2F1tkAFA5FdRXQwfHTkfm21VrUsOSR8s2vUdARO58QGJAdi%2BZX7JNPwJX4ayFA0OgzSIpER54jm3gP8f%2Bt5kH035dXAWP2ty7Y%2Bx8pNZTyEkYe7nnc928BLQ%3D%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20220620T202908Z&X-Amz-SignedHeaders=host&X-Amz-Expires=43200&X-Amz-Credential=ASIASMR4IGCPVCZCE7WJ%2F20220620%2Fus-east-2%2Fs3%2Faws4_request&X-Amz-Signature=0bda2ec4497dd73fee2d6745140afff30c2af7bec4932b73dfb5d6424f6d4a5e',
    }
  },
  activated() {
    this.$fetch()
  },
  async fetch() {
    this.chart_data = await fetch(this.URL).then((res) => res.json())

    const cols = []

    console.log('test')
    console.log(this.chart_data.chart_data[0])

    const data = this.chart_data.chart_data[0].data
    for (const i in data) {
      console.log(data[i])
      cols.push([data[i].key, data[i].value])
    }

    console.log(cols)

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
