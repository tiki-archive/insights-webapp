<template>
  <div class="pageContainer">
    <!-- <search-bar /> -->

    <!-- <h1 class="titleText">Search page {{ slug }}</h1> -->
    <span class="topResult">
      <h1 class="titleText">Top Result</h1>

      <top-result-card
        title="Global Boot Market"
        image="https://cdn.shopify.com/s/files/1/0419/1525/products/1024x1024-Men-Captain-Tobacco-1_672x672.jpg"
        author="TIKI"
        result_type="Dashboard"
      />
    </span>

    <span class="insightResults">
      <h1 class="titleText">Top Insights</h1>

      <insight-list />
    </span>

    <h2>Companies</h2>
    <tall-card-list class="mostRelevant" />

    <h2>Dashboards</h2>
    <tall-card-list class="mostRelevant" />
  </div>
</template>

<script>
import TopResultCard from '~/components/top_result_card/TopResultCard.vue'
import InsightList from '~/components/insight_list/InsightList.vue'

export default {
  name: 'HomeFull',
  components: { TopResultCard, InsightList },
  data() {
    return {
      slug: this.$route.params.search,
    }
  },
  created() {
    this.$root.$emit('enableSearch')
  },
  scrollToTop: true,
}
</script>

<style scoped lang="sass">
@import "assets/styles/theme"

.pageContainer
  margin: 24px 32px 0
  overflow: hidden
  position: relative

  display: block

.topResult
  width: 40%
  margin: auto 10% auto 0
  display: inline-block
  vertical-align: top

.insightResults
  width: 40%
  margin: auto 0 auto auto
  display: inline-block
  vertical-align: top

.titleText, .mostRelevant
  margin: 70px 0 16px
</style>
