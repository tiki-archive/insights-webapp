<!-- Please remove this file from your project -->
<template>
  <a class="sidebarNavItem" href="${href}">
    <inline-svg
      class="navIcon"
      :src="require(`~/assets/images/svg/${icon}.svg`)"
    />
    <span class="navText">{{ text }}</span>
  </a>
</template>

<script>
import InlineSvg from 'vue-inline-svg'

export default {
  components: { InlineSvg },
  props: ['text', 'icon', 'selected', 'href'],
}
</script>

<style scoped lang="sass">
@import "assets/styles/theme"

.sidebarNavItem
  display: flex
  height: 40px
  gap: 16px
  text-decoration: none

.navIcon
  display: block
  width: 24px
  height: 24px
  margin: auto 0

.navText
  color: white
  font-size: 0.875rem
  line-height: 1rem
  margin: auto 0
  font-weight: 800
</style>
