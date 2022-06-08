<template>
  <div class="pageContainer">
    <utils-svg-cmp class="logo" name="tiki_logo" />

    <span class="errorContainer">
      <h1>{{ error.message }}</h1>
      <span v-if="error.details" class="details">{{ error.details }}</span>
      <span v-if="error.statusCode === 404" class="details"
        >We could not find the page you are looking for.</span
      >
    </span>

    <nuxt-link class="homeButton" to="/">
      <span>Home</span>
    </nuxt-link>

    <div class="curve"></div>

    <span class="decoration">
      <utils-svg-cmp name="tiki_guy_eating_pizza" />
    </span>
  </div>
</template>

<script>
import UtilsSvgCmp from '~/components/utils/UtilsSvgCmp.vue'

export default {
  components: { UtilsSvgCmp },
  name: 'ErrorLayout',
  layout: 'plain',
  props: ['error'],
}
</script>

<style scoped lang="sass">
@import "assets/styles/theme"

.pageContainer
  display: flex
  padding: auto auto

  width: 100vw
  height: 100vh

  flex-direction: column

  justify-content: center
  align-items: center

  background-color: white

  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='200 -25 1280 320'%3E%3Cpath fill='%23f3f4f5' fill-opacity='1' d='M0 224L48 197.3C96 171 192 117 288 117.3C384 117 480 171 576 213.3C672 256 768 288 864 288C960 288 1056 256 1152 234.7C1248 213 1344 203 1392 197.3L1440 192L1440 320L1392 320C1344 320 1248 320 1152 320C1056 320 960 320 864 320C768 320 672 320 576 320C480 320 384 320 288 320C192 320 96 320 48 320L0 320Z'%3E%3C/path%3E%3C/svg%3E")
  background-attachment: fixed
  background-size: cover

.logo
  width: max(10vw, 192px)
  margin: 0 0

.tiki_logo
  fill: $tiki-purple

.errorContainer
  display: flex
  flex-direction: column
.details
  margin: auto

.homeButton
  padding: 16px 32px
  background-color: $tiki-purple
  border-radius: 500px

  color: white
  text-decoration: none

  margin: 20px auto

  transition: all .1s ease-in-out

  &:hover
    transform: scale(1.05)

.decoration
  height: max(27vw, 270px)
  width: max(20vw, 180px)
  position: fixed
  bottom: 0
  right: 0

.decoration > svg
  position: absolute
  right: 0
  bottom: 0
  height: 100%
  width: 100%

h1
  color: black

  margin: 20px auto 16px

  text-align: center

  font-size: 2rem
  font-weight: 800

  letter-spacing: -0.04em
</style>
