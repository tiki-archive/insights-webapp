<template>
  <NuxtLink class="insightCard" :to="destination == null ? '' : destination">
    <utils-svg-cmp class="insightImage" :name="icon" />

    <span class="insightInfo">
      <span class="themeCardTitleText">{{ name }}</span>
      <span class="themeCardDescText">{{ description }}</span>
    </span>

    <span class="insightConfidence" v-if="confidence_level != null"
      >{{ confidence_level }}% CL</span
    >

    <div class="tooltip" v-if="confidence_level != null">
      <utils-svg-cmp class="questionMark" name="icon_question_mark" />

      <span class="tooltiptext">
        Confidence level is calculated using the number of users contributing to
        this insight.
      </span>
    </div>
  </NuxtLink>
</template>

<script>
export default {
  props: ['icon', 'name', 'description', 'confidence_level', 'destination'],
}
</script>

<style lang="sass" scoped>
@import "assets/styles/theme/default"

.insightCard
  height: 65px
  width: 100%
  border-radius: 4px
  padding: 0px 8px

  text-decoration: none
  display: flex

.insightImage
  height: 45px
  margin: auto 0

.insightInfo
  margin: auto 0
  padding-left: $page-col-gap

  display: flex
  flex-direction: column
.insightConfidence
  color: $gray

  margin: auto 0 auto auto

  font-size: 0.875rem
  line-height: 1rem
  font-weight: 600

.questionMark
  margin: auto 0
  color: $gray
  font-size: .75rem
  padding-bottom: .875rem

.tooltip
  margin: auto 0

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
  right: 0
  max-width: 10vw
  z-index: 1

.tooltip:hover .tooltiptext
  visibility: visible
</style>
