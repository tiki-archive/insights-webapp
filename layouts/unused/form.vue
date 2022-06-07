<template>
  <div class="formPage">
    <div class="formPageContainer">
      <NuxtLink to="/" class="header">
        <utils-svg-cmp class="logo" name="tiki_logo" />
      </NuxtLink>

      <span class="pageContent">
        <Nuxt id="nuxt" />
      </span>
    </div>
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

body
  margin: 0
  font-family: $font-family-nunito-sans

  overflow: visible

.formPage
  width: 100%

  overflow-x: hidden
  overflow-y: scroll

  display: flex

  margin: auto auto

.formPageContainer
  background: url("assets/images/svg/tiki_guy_happy.svg") 10% 70%/35vw no-repeat fixed,

  width: 100%
  min-height: 100vh

  display: flex
  padding: 0 0 0 40vw

  flex-direction: column

  justify-content: center
  align-items: center

.header
  padding-top: 40px

.logo
  width: max(10vw, 192px)
  margin: 20px auto

.tiki_logo
  fill: $tiki-purple

.pageContent
  width: 30vw

  & > img
    width: 100%

.submitButton
  padding: 16px 48px
  background-color: $tiki-purple
  border-radius: 500px

  color: white
  text-decoration: none

  margin: 20px auto

  transition: all .1s ease-in-out

  &:hover
    transform: scale(1.05)

.otherAction
  font-size: 1rem

  font-weight: 400
  letter-spacing: 0px

  padding-bottom: 50px

  text-align: center

.otherActionLink
  color: $tiki-purple
  text-decoration: underline

  &:hover
    color: $tiki-pink
</style>
