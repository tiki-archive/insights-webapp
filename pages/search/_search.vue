<template>
  <div class="pageContainer">
    <!-- <search-bar /> -->

    <div class="searchResultsContainer">
      <span class="topResult">
        <h2 class="titleText">Top Result</h2>

        <top-result-card
          title="Global Boot Market"
          image="https://cdn.shopify.com/s/files/1/0419/1525/products/1024x1024-Men-Captain-Tobacco-1_672x672.jpg"
          author="TIKI"
          result_type="Dashboard"
          class="topCard"
        />
      </span>

      <span class="secondaryResult">
        <h2 class="titleText">Top Insights</h2>

        <insight-list />
      </span>

      <span class="gridRow">
        <h2>Companies</h2>
        <tall-card-list class="mostRelevant" />
      </span>

      <span class="gridRow">
        <h2>Companies 2</h2>
        <tall-card-list class="mostRelevant" />
      </span>

      <span class="gridRow">
        <h2>Companies 3</h2>
        <tall-card-list class="mostRelevant" />
      </span>
    </div>

    <!-- <h1 class="titleText">Search page {{ slug }}</h1> -->
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

.searchResultsContainer
  display: flex
  flex-wrap: wrap

  column-gap: 24px
  row-gap: 32px

  margin-top: 5vh

  justify-content: space-between

.topResult
  box-sizing: border-box

  display: flex

  flex-direction: column

  flex: 0 0 2

.topCard
  height: 260px

.secondaryResult
  flex-basis: 6
  flex-grow: 6
  flex-shrink: 0

.gridRow
  flex-basis: 100%
</style>
