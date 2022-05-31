<template>
  <NuxtLink
    class="sidebarNavItemContainer"
    :to="destination"
    :class="[selected == 'true' ? 'currentlySelected' : '']"
  >
    <inline-svg
      class="navIcon"
      :src="require(`~/assets/images/svg/${icon}.svg`)"
    />
    <span class="navText">{{ text }}</span>
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
@import "assets/styles/mixins"

.sidebarNavItemContainer
  display: flex
  height: 40px
  gap: 16px
  text-decoration: none

.navIcon
  margin: auto 0

  width: 24px
  height: 24px

  fill: $text-gray

   // Make it glow white while hovering, or if it is currently selected
  :hover > &, .currentlySelected > &
    -webkit-filter: brightness(1.3)
    -moz-filter: brightness(1.3)
    -ms-filter: brightness(1.3)
    filter: brightness(1.3)

.navText
  margin: auto 0

  font-size: 0.875rem
  line-height: 1rem
  font-weight: 800

  color: $text-gray

  // Make it glow white while hovering, or if it is currently selected
  :hover > &, .currentlySelected > &
    color: white

@include for-phone

  .sidebarNavItemContainer
    height: 52px
    gap: 20px

  .navIcon
    width: 36px
    height: 36px

  .navText
    font-size: 1.25rem
    line-height: 2.0rem
    font-weight: 400
</style>
