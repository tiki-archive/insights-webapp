<template>
  <div class="page">
    <span class="sideContainer">
      <sidebar-full-vue />
    </span>

    <span class="mainContainer">
      <home-page-full-view />
    </span>
  </div>
</template>

<script>
import HomePageFullView from '~/components/home/HomePageFull.vue'
import SidebarFullVue from '~/components/sidebar/SidebarFull.vue'

export default {
  name: 'IndexPage',
  components: {
    SidebarFullVue,
    HomePageFullView,
  },
  head() {
    return {
      title: 'TIKI Insights | Home',
    }
  },
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

.mainContainer
  width: calc(100vw - 241px) // this is loose as hell
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
