<!-- Please remove this file from your project -->
<template>
  <div class="sidebar">
    <div class="sidebarContent">
      <a href="/">
        <tiki-logo class="sidebarLogo" />
      </a>
    </div>

    <div class="sidebarContent">
      <sidebar-nav-item
        text="Home"
        icon="home_icon"
        href="apple.com"
        selected="true"
      />
      <sidebar-nav-item text="Search" icon="search_icon" href="apple.com" />
      <sidebar-nav-item
        text="Your Library"
        icon="library_icon"
        href="apple.com"
      />
    </div>
  </div>
</template>

<script>
import TikiLogo from '../general/TikiLogo.vue'
import SidebarNavItem from './SidebarNavItem.vue'
export default {
  components: { TikiLogo, SidebarNavItem },
  name: 'NuxtTutorial',
}
</script>

<style scoped lang="sass">
@import "assets/styles/theme"

.sidebar
  width: 241px
  height: 100vh
  color: white
  background: $tiki-purple

.sidebarContent
  padding: 24px 24px 0 24px

.sidebarLogo
  max-height: 38px
</style>
