<template>
  <div class="page">
    <span class="sideContainer">
      <sidebar />
    </span>

    <span class="mainContainer">
      <navbar
        name="Nick"
        icon="https://s3-alpha.figma.com/profile/6da8521c-f18e-47e3-961f-c6f765fc4014"
      />
      <Nuxt id="nuxt" />
    </span>
  </div>
</template>

<script>
import Navbar from '~/components/navbar/Navbar.vue'
export default {
  components: { Navbar },
  name: 'DefaultLayout',
}
</script>

<style scoped lang="sass">
@import "assets/styles/mixins"

.page
  width: 100%
  height: 100vh
  background: linear-gradient(0deg, #27002E 0%, rgba(39, 0, 46, 0.881875) 37.5%, rgba(39, 0, 46, 0.82) 100%)

  overflow: hidden

  display: flex

  z-index: 100

#navbar // this works because the navbar id is given in the component for its own scroll logic
  z-index: 100

#nuxt
  z-index: 10

.mainContainer
  width: calc(100vw - 243px) // this is loose as hell
  max-height: 100vh

  overflow-y: scroll

::-webkit-scrollbar
  width: 12px

::-webkit-scrollbar-track
  display: hidden

::-webkit-scrollbar-thumb
  background-color: rgb(179, 179, 179)

@include for-phone
  .page
    display: block
    overflow-y: scroll
</style>

<style lang="sass">
@import "assets/styles/theme"

body
  margin: 0
  font-family: $font-family-nunito-sans

::-webkit-scrollbar
  width: 12px

::-webkit-scrollbar-track
  display: hidden

::-webkit-scrollbar-thumb
  background-color: rgb(179, 179, 179)
</style>
