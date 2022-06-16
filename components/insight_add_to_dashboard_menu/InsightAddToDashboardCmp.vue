<template>
  <full-page-popup @clickedOut="clickedOut">
    <span class="insightAddToDashboard">
      <section>
        <span class="headerText">
          <span>Add to dashboard</span>

          <span class="tooltip">
            <utils-svg-cmp class="questionMark" name="icon_question_mark" />

            <span class="tooltiptext">
              Dashboards are pages you can create to view multiple insights in
              one handy place. Add this insight to a dashboard by selecting the
              dashboard on the right.
            </span>
          </span>
        </span>
        <utils-svg-cmp name="add_insight_to_dashboard_graphic" />
      </section>

      <section>
        <insight-add-to-dashboard-list
          :dashboards="[
            { name: 'Our Competitors' },
            { name: 'Cross-sell / Up-sell' },
            { name: 'Target demos' },
            { name: 'Boots' },
            { name: 'Tech Companies' },
            { name: 'Big Chocolate' },
          ]"
        />
      </section>
    </span>
  </full-page-popup>
</template>

<script>
import FullPagePopup from '../fullpage_popup/FullPagePopupCmp.vue'
import UtilsSvgCmp from '../utils/UtilsSvgCmp.vue'
import InsightAddToDashboardList from './InsightAddToDashboardListCmp.vue'
export default {
  components: { FullPagePopup, UtilsSvgCmp, InsightAddToDashboardList },
  name: 'InsightAddToDashboard',
  props: ['insight', 'dashboards'],
  methods: {
    clickedOut() {
      this.$emit('clickedOut')
    },
  },
}
</script>

<style scoped lang="sass">
@import "assets/styles/theme/default"

.insightAddToDashboard
  width: 100%
  height: 100%

  display: flex
  padding: 32px 16px

  box-sizing: border-box

section
  margin: auto auto
  width: 50%
  height: 100%

  display: flex
  align-items: center
  justify-content: center
  flex-direction: column

.questionMark
  font-size: 1.25rem
  padding-left: 8px
.headerText
  display: flex
  text-align: center
  font-size: 2rem
  font-weight: 700
  margin-bottom: 24px
.tooltip
  margin: 0 0 auto

.tooltip .tooltiptext
  visibility: hidden
  background-color: black
  color: #fff

  font-size: .75rem
  font-weight: 400

  border-radius: 6px
  padding: 5px 5px

  /* Position the tooltip */
  position: absolute

  max-width: 10vw
  z-index: 1

.tooltip:hover .tooltiptext
  visibility: visible
</style>
