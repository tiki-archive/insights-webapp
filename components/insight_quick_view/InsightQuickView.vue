<template>
  <NuxtLink class="insightCard" :to="insightLink">
    <div class="cardContent">
      <div class="cardInfo">
        <h2 class="cardTitle">{{ title }}</h2>
        <p class="cardDesc">{{ description }}</p>
      </div>

      <img class="cardImage" :src="source" />

      <NuxtLink class="seeMore" to="">
        <utils-svg-cmp name="icon_three_dots" />
      </NuxtLink>
    </div>
  </NuxtLink>
</template>

<script>
import UtilsSvgCmp from '../utils/UtilsSvgCmp.vue'
export default {
  components: { UtilsSvgCmp },
  props: ['title', 'description', 'source', 'insightLink'],
}
</script>

<style lang="sass" scoped>
@import "assets/styles/theme"

.insightCard
  width: 100%

  text-decoration: none

.cardContent
  margin: 0 auto
  padding: 16px

  position: relative

  background: rgba(84, 84, 84, 0.25)

  border-radius: 8px

  &:hover
    background: rgba(84, 84, 84, 0.4)

.cardImage
  width: 90%
  margin: 0px 5% 12px

.cardInfo
  overflow: hidden
  padding-top: 12px
  padding-left: 16px

.cardTitle
  color: white
  margin: 0

  font-size: 1.25rem

  font-weight: 700

  white-space: nowrap
  overflow: hidden
  text-overflow: ellipsis

.cardDesc
  color: $text-gray

  font-size: 0.875rem
  line-height: 1rem

  padding-top: 4px
  margin: 0

  display: -webkit-box
  -webkit-box-orient: vertical
  -webkit-line-clamp: 2
  text-overflow: ellipsis
.seeMore
  position: absolute
  top: 0
  right: 0
  padding: 16px

  &:hover
    -webkit-filter: brightness(1.3)
    -moz-filter: brightness(1.3)
    -ms-filter: brightness(1.3)
    filter: brightness(1.3)
</style>
