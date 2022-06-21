<template>
  <div class="insightNavbar">
    <button @click="addToDashboard">
      <utils-svg-cmp name="icon_add_insight_to_dashboard" />
    </button>

    <button @click="addToPipeline">
      <utils-svg-cmp name="icon_add_insight_to_pipeline" />
    </button>

    <insight-navbar-filter icon="icon_filter_date" text="Last 30 days" />
    <insight-navbar-filter icon="icon_location_pin" text="USA" />
  </div>
</template>

<script>
import UtilsSvgCmp from '../utils/UtilsSvgCmp.vue'
import InsightNavbarFilter from './InsightNavbarFilterCmp.vue'
export default {
  components: { UtilsSvgCmp, InsightNavbarFilter },
  props: [],
  methods: {
    addToDashboard() {
      this.$emit('addToDashboard')
    },
    addToPipeline() {
      this.$emit('addToPipeline')
    },
  },
}
</script>

<style scoped lang="sass">
@import "assets/styles/theme"

.insightNavbar
  width: 100%
  display: flex
  gap: 16px

  align-items: center

button
  border: 0
  padding: 0
  background: none

  cursor: pointer

  > svg
    width: 32px
    opacity: 0.85

  &:hover
    > svg
      opacity: 1.0
</style>
