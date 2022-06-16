<template>
  <div class="themeStandardPageContainer">
    <span class="headerInfo">
      <span class="themeHeaderLabel">Dashboard</span>
      <span class="themeBigHeaderText">Our Competitors</span>
    </span>

    <section class="themeMultiContentSection">
      <insight-quick-view
        title="Dr Martins"
        description="Best Email Subject Lines"
        source="https://gyazo.com/dd876436e6da92f755591429e050036a.png"
        insightLink="test"
        class="insightChart"
      />
      <insight-quick-view
        title="Dr Martins"
        description="Best Email Subject Lines"
        source="https://gyazo.com/dd876436e6da92f755591429e050036a.png"
        insightLink="test"
        class="insightChart"
      />
      <insight-quick-view
        title="Dr Martins"
        description="Best Email Subject Lines"
        source="https://gyazo.com/dd876436e6da92f755591429e050036a.png"
        insightLink="test"
        class="insightChart"
      />
      <insight-quick-view
        title="Dr Martins"
        description="Best Email Subject Lines"
        source="https://gyazo.com/dd876436e6da92f755591429e050036a.png"
        insightLink="test"
        class="insightChart"
      />
    </section>
  </div>
</template>

<script>
import InsightQuickView from '~/components/insight_quick_view/InsightQuickView.vue'
export default {
  components: { InsightQuickView },
  data() {
    return {
      slug: this.$route.params.dashboard,
    }
  },
}
</script>

<style scoped lang="sass">
@import "assets/styles/theme/default"
.headerInfo
  display: flex
  flex-direction: column

.themeMultiContentSection
  display: grid

  grid-template: auto/repeat(auto-fill,minmax(max(320px,34%),1fr))

  grid-column-gap: $page-col-gap
  grid-row-gap: $page-row-gap
</style>
