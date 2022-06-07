<template>
  <div class="defaultPage">
    <span class="sideContainer pcOnly">
      <sidebar />
    </span>

    <span class="mainContainer pcOnly">
      <!-- This feels absolutely disgusting but I haven't found a nicer way
          I think the alternative is moving nav bar into individual pages or
          having the search bar separate from nav. The ladder would be odd with
          scrolling -->
      <navbar
        name="Nick"
        icon="https://s3-alpha.figma.com/profile/6da8521c-f18e-47e3-961f-c6f765fc4014"
        :showSearch="$nuxt.$route.path.startsWith('/search')"
      />

      <Nuxt id="nuxt" />
    </span>

    <span class="phoneOnly">
      <notify-use-desktop />
    </span>
  </div>
</template>

<script>
import NotifyUseDesktop from '~/components/notify_use_desktop/NotifyUseDesktop.vue'
import Sidebar from '~/components/sidebar/Sidebar.vue'

export default {
  components: { Sidebar, NotifyUseDesktop },
  name: 'DefaultLayout',
  data() {
    return {
      searchEnabled: false,
    }
  },
  methods: {
    enableSearch() {
      this.searchEnabled = true
    },
  },
  beforeRouteEnter(to, from, next) {
    console.log('FROMM ' + from)
  },

  scrollToTop: true,
}
</script>

<style lang="sass">
@import "assets/styles/theme"
@import "assets/styles/mixins"

body
  margin: 0
  font-family: $font-family-nunito-sans

  overflow: hidden

.defaultPage
  width: 100%

  height: 100vh

  background: linear-gradient(0deg, #27002E 0%, rgba(39, 0, 46, 0.881875) 37.5%, rgba(39, 0, 46, 0.82) 100%)

  overflow: hidden

  display: flex

  z-index: 15

.mainContainer
  width: calc(100vw - 243px) // this is loose as hell
  max-height: 100vh

  box-sizing: border-box

  overflow-y: overlay

#navbar // this works because the navbar id is given in the component for its own scroll logic
  z-index: 15

#nuxt
  z-index: 10

::-webkit-scrollbar
  width: 12px

::-webkit-scrollbar-thumb
  background-color: rgb(179, 179, 179)

.phoneOnly
  visibility: hidden
  display: none

.pcOnly
  visibility: visible

@include for-small-screen
  .phoneOnly
    visibility: visible
    display: flex

  .pcOnly
    visibility: hidden
    display: none
</style>
