<template>
  <button class="userButton">
    <img class="userIcon" :src="icon" />
    <span class="userName">{{ name }}</span>
    <utils-svg-cmp class="downArrow" name="icon_down_arrow" />
  </button>
</template>

<script>
import UtilsSvgCmp from '../utils/UtilsSvgCmp.vue'
export default {
  components: { UtilsSvgCmp },
  name: 'SidebarFull',
  props: ['name', 'icon'],
}
</script>

<style scoped lang="sass">
@import "assets/styles/theme"

.userButton
  display: flex
  align-items: center

  border: 0
  border-radius: 23px
  background-color: $tiki-purple

  gap: 8px
  padding: 2px
  height: 32px

  &:hover
    background-color: lighten($tiki-purple, 3%)

.userIcon
  width: 28px
  height: 28px
  display: inline-block

  border-radius: 23px

.userName
  color: white
  font-family: $font-family-nunito-sans
  font-size: .875rem
  font-weight: 700

.downArrow
  margin-right: 8px
</style>
