<template>
  <div class="pageContainer">
    <!-- The top elements of the sidebar which are the same size regardless of device -->
    <span class="pageContent">
      <utils-svg-cmp class="logo" name="tiki_logo" />

      <span class="text"
        >The insights website is only available on desktop at the moment.</span
      >
    </span>
  </div>
</template>

<script>
import UtilsSvgCmp from '../utils/UtilsSvgCmp.vue'
export default {
  components: { UtilsSvgCmp },
  name: 'NotifyUseDesktop',
}
</script>

<style scoped lang="sass">
@import "assets/styles/theme"
@import "assets/styles/mixins"

.pageContainer
  width: 100vw
  height: 100vh
  overflow: hidden

  display: flex

  color: white
  background: $tiki-purple

.pageContent
  display: flex
  flex-flow: column
  margin: auto auto
  padding: 10%

.logo
  fill: white
  max-width: 45vw

  margin: auto auto
  padding-bottom: 30px

.text
  text-align: center
  font-size: 1.5rem
</style>
