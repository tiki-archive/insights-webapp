<template>
  <div class="page">
    <sidebar-full-vue />
  </div>
</template>

<script>
import SidebarFullVue from '~/components/sidebar/SidebarFull.vue'

export default {
  name: 'IndexPage',
  components: {
    SidebarFullVue,
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


::-webkit-scrollbar
  width: 12px

::-webkit-scrollbar-track
  display: hidden

::-webkit-scrollbar-thumb
  background-color: rgb(179, 179, 179)
</style>
