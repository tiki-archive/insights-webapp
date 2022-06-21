<template>
  <div class="themeStandardPageContainer">
    <!-- <search-bar /> -->

    <section class="themeMultiContentSection topSection">
      <span class="topResult">
        <h2 class="titleText">Top results</h2>

        <top-result-card
          title="Global Boot Market"
          image="https://cdn.shopify.com/s/files/1/0419/1525/products/1024x1024-Men-Captain-Tobacco-1_672x672.jpg"
          author="TIKI"
          result_type="Dashboard"
          class="topResultCard"
        />
      </span>

      <span class="secondaryResult">
        <content-heading text="Insights" link="/search/insights/test" />

        <insight-list />
      </span>
    </section>

    <section>
      <content-heading text="Companies" link="/search/companies/test" />

      <tall-card-list />
    </section>

    <section>
      <content-heading text="Dashboards" link="/search/dashboards/test" />

      <tall-card-list />
    </section>
  </div>
</template>

<script>
import TopResultCard from '~/components/top_result_card/TopResultCardCmp.vue'
import InsightList from '~/components/insight_list/InsightListCmp.vue'
import ContentHeading from '~/components/content_heading/ContentHeadingCmp.vue'
import TallCardList from '~/components/tall_card_list/TallCardListCmp.vue'

export default {
  name: 'HomeFull',
  components: {
    TopResultCard,
    InsightList,
    ContentHeading,
    TallCardList,
  },
  data() {
    return {
      searchTerm: this.$route.params.search,
    }
  },
  scrollToTop: true,
}
</script>

<style scoped lang="sass">
@import "assets/styles/theme/default"
.topResultCard
  height: 260px
  width: 30vw

  box-sizing: border-box
.secondaryResult
  min-width: 400px
  width: calc(100% - 30vw - $page-col-gap)
  box-sizing: border-box
</style>
