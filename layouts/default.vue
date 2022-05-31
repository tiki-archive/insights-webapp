<template>
  <div :class="'page' + (showMobileMenu ? ' disableScroll' : '')">
    <span class="sideContainer">
      <span class="mobileOnly">
        <mobile-header @clickedMenuButton="showMobileMenu = !showMobileMenu" />
        <sidebar v-if="showMobileMenu" />
      </span>

      <span class="desktopOnly">
        <sidebar />
      </span>
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
import MobileHeader from '~/components/mobile_header/MobileHeader.vue'
import Navbar from '~/components/navbar/Navbar.vue'
import Sidebar from '~/components/sidebar/Sidebar.vue'
export default {
  components: { Navbar, MobileHeader, Sidebar },
  name: 'DefaultLayout',
  data() {
    return {
      showMobileMenu: false,
    }
  },
  watch: {
    $route() {
      // when user clicks link in mobile menu to go to new route, we should close it
      this.showMobileMenu = false
    },
  },
}
</script>

<style lang="sass">
@import "assets/styles/theme"
@import "assets/styles/mixins"

body
  margin: 0
  font-family: $font-family-nunito-sans

.page
  width: 100%
  height: 100vh
  background: linear-gradient(0deg, #27002E 0%, rgba(39, 0, 46, 0.881875) 37.5%, rgba(39, 0, 46, 0.82) 100%)

  overflow: hidden

  display: flex

  z-index: 100

.mainContainer
  width: calc(100vw - 243px) // this is loose as hell
  max-height: 100vh

  overflow-y: scroll

#navbar // this works because the navbar id is given in the component for its own scroll logic
  z-index: 100

#nuxt
  z-index: 10

@include for-tablet
  .mobileOnly
    display: none !important

  ::-webkit-scrollbar
    width: 12px

  ::-webkit-scrollbar-track
    display: hidden

  ::-webkit-scrollbar-thumb
    background-color: rgb(179, 179, 179)

@include for-phone
  .desktopOnly
    display: none !important // todo: no

  .page
    display: block
    overflow-y: scroll

  .disableScroll
    overflow: hidden

  #navbar
    visibility: hidden
</style>
