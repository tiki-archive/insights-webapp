<template>
  <div class="themeStandardPageContainer">
    <insight-header
      name="Best Subject Lines"
      source="Dr Martens"
      icon="https://gyazo.com/16f7279929955b76d85115e146c08f68.png"
    />

    <insight-navbar
      @addToDashboard="openAddDashboard"
      @addToPipeline="openAddPipeline"
    />

    <section>
      <img src="https://gyazo.com/18cda419411923c058c8ddbf0a703f9b.png" />
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
  margin: auto
  display: flex
</style>
