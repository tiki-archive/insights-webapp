<!-- Please remove this file from your project -->
<template>
  <div class="sidebar">
    <!-- The top elements of the sidebar which are the same size regardless of device -->
    <div class="sidebarTopHalf">
      <div class="sidebarSectionTop">
        <NuxtLink to="/">
          <tiki-logo class="sidebarLogo" />
        </NuxtLink>
      </div>

      <!-- Home, Search, Library -->
      <div class="sidebarSectionTop">
        <sidebar-nav-item
          text="Home"
          icon="icon_home"
          destination=""
          selected="true"
        />
        <sidebar-nav-item text="Search" icon="icon_search" destination="" />
        <sidebar-nav-item
          text="Your Library"
          icon="icon_library"
          destination=""
        />
      </div>

      <!-- Create Dashboard, Liked Insights, Your Company -->
      <div class="sidebarSectionTop">
        <sidebar-nav-item
          text="Create Dashboard"
          icon="icon_add_dashboard"
          destination=""
          selected=""
        />
        <sidebar-nav-item
          text="Liked Insights"
          icon="icon_liked_insights"
          destination=""
        />
        <sidebar-nav-item
          text="Your Company"
          icon="icon_your_company"
          destination=""
        />
      </div>

      <!-- Separating Bar -->
      <hr class="separatingBar" />
    </div>

    <!-- The bottom, scrollable sidebar content taking up the rest of the space -->
    <div class="sidebarBottomHalf">
      <sidebar-dashboard-list
        class="sidebarSectionBottom"
        :dashboards="items"
      />
    </div>
  </div>
</template>

<script>
import TikiLogo from '../general/TikiLogo.vue'
import SidebarDashboardList from './SidebarDashboardList.vue'
import SidebarNavItem from './SidebarNavItem.vue'
export default {
  components: { TikiLogo, SidebarNavItem, SidebarDashboardList },
  name: 'SidebarFull',
  data() {
    return {
      items: [
        { name: 'Some Random Dashboard 1', destination: 'to' },
        { name: 'Some Random Dashboard 2', destination: 'to' },
        { name: 'Some Random Dashboard 3', destination: 'to' },
        { name: 'Some Random Dashboard 4', destination: 'to' },
        { name: 'Some Random Dashboard 1', destination: 'to' },
        { name: 'Some Random Dashboard 2', destination: 'to' },
        { name: 'Some Random Dashboard 3', destination: 'to' },
        { name: 'Some Random Dashboard 4', destination: 'to' },
        { name: 'Some Random Dashboard 1', destination: 'to' },
        { name: 'Some Random Dashboard 2', destination: 'to' },
        { name: 'Some Random Dashboard 3', destination: 'to' },
        { name: 'Some Random Dashboard 4', destination: 'to' },
        { name: 'Some Random Dashboard 1', destination: 'to' },
        { name: 'Some Random Dashboard 2', destination: 'to' },
        { name: 'Some Random Dashboard 3', destination: 'to' },
        { name: 'Some Random Dashboard 4', destination: 'to' },
        { name: 'Some Random Dashboard 1', destination: 'to' },
        { name: 'Some Random Dashboard 2', destination: 'to' },
        { name: 'Some Random Dashboard 3', destination: 'to' },
        { name: 'Some Random Dashboard 4', destination: 'to' },
        { name: 'Some Random Dashboard 1', destination: 'to' },
        { name: 'Some Random Dashboard 2', destination: 'to' },
        { name: 'Some Random Dashboard 3', destination: 'to' },
        { name: 'Some Random Dashboard 4', destination: 'to' },
        { name: 'Some Random Dashboard 1', destination: 'to' },
        { name: 'Some Random Dashboard 2', destination: 'to' },
        { name: 'Some Random Dashboard 3', destination: 'to' },
        { name: 'Some Random Dashboard 4', destination: 'to' },
      ],
    }
  },
}
</script>

<style scoped lang="sass">
@import "assets/styles/theme"

.sidebar
  width: 241px
  height: 100vh
  overflow: hidden

  display: table

  color: white
  background: $tiki-purple

.sidebarLogo
  max-height: 38px

.sidebarTopHalf
  display: table-row
  height: 0

.sidebarSectionTop
  padding: 24px 24px 0 24px

.separatingBar
  background-color: rgba(84, 84, 84, 0.75)
  border: none
  height: 1px
  margin: 8px 24px 0 24px
  min-height: 1px

.sidebarBottomHalf
  display: table-row
  height: auto

.sidebarSectionBottom
  margin-left: 24px
</style>
