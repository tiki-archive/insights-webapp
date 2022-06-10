<template>
  <div class="pageContainer">
    <h1 class="titleText">I am a dashboard page for {{ slug }}</h1>

    <insight-quick-view
      title="Dr Martins"
      description="Best Email Subject Lines"
      source="https://gyazo.com/dd876436e6da92f755591429e050036a.png"
      insightLink="test"
    />
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
@import "assets/styles/theme"

.pageContainer
  margin: auto 32px
  padding-top: 1.75vh
  overflow: hidden
  position: relative

.titleText
  margin: 70px 0 16px
</style>
