<template>
  <div class="formPage">
    <TrackedNuxtLink to="/" class="header">
      <utils-svg-cmp class="logo" name="tiki_logo" width="100%" />
    </TrackedNuxtLink>

    <span class="pageContent">
      <Nuxt id="nuxt" />
    </span>
  </div>
</template>

<script>
import UtilsSvgCmp from '~/components/utils/UtilsSvgCmp.vue'
export default {
  components: { UtilsSvgCmp },
  name: 'FormLayout',
}
</script>

<style lang="sass">
@import "assets/styles/theme"
@import "assets/styles/mixins"

.formPage
  width: 100%
  min-height: 100vh

  background: url("assets/images/svg/tiki_guy_happy.svg") 10% 70%/35vw no-repeat fixed,

  overflow-x: hidden
  overflow-y: scroll

  display: flex

  padding: 0 0 0 40vw

  box-sizing: border-box

  flex-direction: column
  justify-content: center
  align-items: center

.header
  width: max(10vw, 192px)
  margin: 20px auto

.tiki_logo
  fill: $tiki-purple

.pageContent
  width: 30vw

  & > img
    width: 100%
</style>
