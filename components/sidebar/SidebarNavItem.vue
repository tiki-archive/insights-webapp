<template>
  <NuxtLink class="sidebarNavItemContainer" :to="destination">
    <inline-svg
      v-bind:class="[
        selected == 'true' ? 'navIcon currentlySelected' : 'navIcon',
      ]"
      :src="require(`~/assets/images/svg/${icon}.svg`)"
    />
    <span
      v-bind:class="[
        selected == 'true' ? 'navText currentlySelected' : 'navText',
      ]"
      >{{ text }}</span
    >
  </NuxtLink>
</template>

<script>
import InlineSvg from 'vue-inline-svg'

export default {
  components: { InlineSvg },
  props: ['text', 'icon', 'selected', 'destination'],
}
</script>

<style scoped lang="sass">
@import "assets/styles/theme"

.sidebarNavItemContainer
  display: flex
  width: 100%
  height: 40px
  gap: 16px
  text-decoration: none

.navIcon
  display: block
  margin: auto 0

  width: 24px
  height: 24px

  fill: $text-gray

   // Make it glow white while hovering, or if it is currently selected
  :hover > &, &.currentlySelected
    -webkit-filter: brightness(1.3)
    -moz-filter: brightness(1.3)
    -ms-filter: brightness(1.3)
    filter: brightness(1.3)


.navText
  margin: auto  0

  font-size: 0.875rem
  line-height: 1rem
  font-weight: 800

  color: $text-gray

  // Make it glow white while hovering, or if it is currently selected
  :hover > &, &.currentlySelected
    color: white
</style>
