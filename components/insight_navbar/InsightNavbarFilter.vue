<template>
  <button class="insightNavbarFilter">
    <utils-svg-cmp class="navIcon" :name="icon" />
    <span class="text">{{ text }}</span>
  </button>
</template>

<script>
import UtilsSvgCmp from '../utils/UtilsSvgCmp.vue'

export default {
  components: { UtilsSvgCmp },
  props: ['text', 'icon'],
}
</script>

<style scoped lang="sass">
@import "assets/styles/theme"
@import "assets/styles/mixins"

.insightNavbarFilter
  display: flex
  height: 32px

  gap: 8px
  padding: 16px

  border: solid $text-gray 2px
  border-radius: 8px

  justify-content: center
  align-items: center
  text-align: center

  text-decoration: none

  &:hover
    -webkit-filter: brightness(1.3)
    -moz-filter: brightness(1.3)
    -ms-filter: brightness(1.3)
    filter: brightness(1.3)
.navIcon
  max-height: 20px
  max-width: 20px
.text
  font-size: 1rem
  font-family: $font-family-nunito-sans

  color: $text-gray

svg
  fill: $text-gray
</style>
