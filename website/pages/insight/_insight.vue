<template>
  <div class="themeStandardPageContainer">
    <insight-header
      name="Top Subject Lines"
      source="Dr Martens"
      icon="https://www.cravingsofalunatic.com/wp-content/uploads/2014/01/Birthday-Giveaway.png"
    />

    <insight-navbar
      @addToDashboard="openAddDashboard"
      @addToPipeline="openAddPipeline"
    />

    <section>
      <pie-chart-cmp />
      <!-- <img src="https://i.gyazo.com/dd876436e6da92f755591429e050036a.png" /> -->
    </section>

    <section>
      <TitleDescription
        title="Description"
        description="The Customer Location insight details the number of customers purchasing items from the brand. The insight may be helpful in determining target markets, competitive opportunities, or optimizing marketing spend."
      />
    </section>

    <section>
      <content-heading text="Insights" link="test" />

      <wide-card-list />
    </section>

    <insight-add-to-dashboard
      v-if="this.addToDashboard"
      @clickedOut="closeAddDashboard"
    />

    <insight-add-to-pipeline
      v-if="this.addToPipeline"
      @clickedOut="closeAddPipeline"
    />
  </div>
</template>

<script>
import PieChartCmp from '~/components/charts/pie/PieChartCmp.vue'
import InsightAddToDashboard from '~/components/insight_add_to_dashboard_menu/InsightAddToDashboardCmp.vue'
import InsightHeader from '~/components/insight_header/InsightHeaderCmp.vue'
import InsightNavbar from '~/components/insight_navbar/InsightNavbarCmp.vue'
import TitleDescription from '~/components/title_description/TitleDescriptionCmp.vue'
import WideCardList from '~/components/wide_card_list/WideCardListCmp.vue'

export default {
  components: {
    InsightHeader,
    TitleDescription,
    InsightAddToDashboard,
    InsightNavbar,
    WideCardList,
    PieChartCmp,
  },
  data() {
    return {
      addToDashboard: false,
      addToPipeline: false,
      slug: this.$route.params.insight,
      filters: this.$route.query.location,
    }
  },
  methods: {
    openAddDashboard() {
      console.log('Open add dashboard')
      this.addToDashboard = true
    },
    closeAddDashboard() {
      console.log('close add dashboard')
      this.addToDashboard = false
    },
    openAddPipeline() {
      console.log('Open add pipeline')
      this.addToPipeline = true
    },
    closeAddPipeline() {
      console.log('close add pipeline')
      this.addToPipeline = false
    },
  },
}
</script>

<style scoped lang="sass">
@import "assets/styles/theme/default"

img
  width: 50%
  margin: auto
  display: flex
</style>
