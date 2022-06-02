<template>
  <div class="pageContainer">
    <!-- <search-bar /> -->

    <div class="searchResultsContainer">
      <span class="topResult">
        <h2 class="titleText">Top result {{ slug }}</h2>

        <top-result-card
          title="Global Boot Market"
          image="https://cdn.shopify.com/s/files/1/0419/1525/products/1024x1024-Men-Captain-Tobacco-1_672x672.jpg"
          author="TIKI"
          result_type="Dashboard"
          class="topCard"
        />
      </span>

      <span class="secondaryResult">
        <span class="heading">
          <h2>
            <NuxtLink
              class="headingLink"
              :to="'/search/insights/' + searchTerm"
            >
              Insights
            </NuxtLink>
          </h2>

          <NuxtLink class="seeAll" :to="'/search/insights/' + searchTerm">
            SEE ALL
          </NuxtLink>
        </span>

        <insight-list />
      </span>

      <span class="gridRow">
        <span class="heading">
          <h2>
            <NuxtLink
              class="headingLink"
              :to="'/search/companies/' + searchTerm"
            >
              Companies
            </NuxtLink>
          </h2>

          <NuxtLink class="seeAll" :to="'/search/companies/' + searchTerm">
            SEE ALL
          </NuxtLink>
        </span>

        <tall-card-list />
      </span>

      <span class="gridRow">
        <span class="heading">
          <h2>
            <NuxtLink
              class="headingLink"
              :to="'/search/dashboard/' + searchTerm"
            >
              Dashboards
            </NuxtLink>
          </h2>

          <NuxtLink class="seeAll" :to="'/search/dashboard/' + searchTerm">
            SEE ALL
          </NuxtLink>
        </span>

        <tall-card-list />
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
      searchTerm: this.$route.params.search,
    }
  },
  scrollToTop: true,
}
</script>

<style scoped lang="sass">
@import "assets/styles/theme"

.pageContainer
  margin: calc(4vh + 24px) 32px 0 32px
  overflow: hidden
  position: relative

  display: block

.searchResultsContainer
  display: grid

  grid-template: 332px/repeat(auto-fill,minmax(max(180px,10%),1fr))
  grid-column-gap: 24px
  grid-row-gap: min(2.2vh, 22px)

  justify-content: space-between

.topResult
  grid-column: 1 / 3
  height: 260px

.secondaryResult
  grid-column: 3 / -1

.gridRow
   grid-column: 1 / -1

.heading
  display: flex

h2
  margin: 16px 0

.seeAll
  color: $see-all-text
  font-weight: 800
  font-size: .875rem
  text-decoration: none

  margin: auto 0 auto auto

  &:hover
    text-decoration: underline

.headingLink
  text-decoration: none
  color: white

  &:hover
    text-decoration: underline
</style>
