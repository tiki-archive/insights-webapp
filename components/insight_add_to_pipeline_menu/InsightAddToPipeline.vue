<template>
  <full-page-popup @clickedOut="clickedOut">
    <span class="insightAddToPipeline">
      <section>
        <span class="headerText">
          <span>Connect to data</span>

          <span class="tooltip">
            <utils-svg-cmp class="questionMark" name="icon_question_mark" />

            <span class="tooltiptext">
              Connect this insight to an external date pipeline to process it
              yourself.
            </span>
          </span>
        </span>
        <utils-svg-cmp name="add_insight_to_pipeline_graphic" />
      </section>

      <section>
        <insight-add-to-pipeline-list
          :pipelines="[
            { name: 'Tableau', icon: 'icon_pipeline_tableau' },
            { name: 'Domo', icon: 'icon_pipeline_domo' },
            { name: 'Looker', icon: 'icon_pipeline_looker' },
            { name: 'API', icon: 'icon_pipeline_arrows' },
          ]"
        />
      </section>
    </span>
  </full-page-popup>
</template>

<script>
import FullPagePopup from '../fullpage_popup/FullPagePopup.vue'
import UtilsSvgCmp from '../utils/UtilsSvgCmp.vue'
import InsightAddToPipelineList from './InsightAddToPipelineList.vue'

export default {
  components: { FullPagePopup, UtilsSvgCmp, InsightAddToPipelineList },
  name: 'InsightAddToPipeline',
  props: ['insight'],
  methods: {
    clickedOut() {
      this.$emit('clickedOut')
    },
  },
}
</script>

<style scoped lang="sass">
@import "assets/styles/theme/default"

.insightAddToPipeline
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
