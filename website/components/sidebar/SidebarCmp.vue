<template>
  <div class="sidebar">
    <!-- The top elements of the sidebar which are the same size regardless of device -->
    <div>
      <div class="sidebarSectionPadded sidebarLogoContainer">
        <NuxtLink to="/">
          <utils-svg-cmp class="sidebarLogo" name="tiki_logo" />
        </NuxtLink>
      </div>

      <!-- Home, Search, Library -->
      <div class="sidebarSectionPadded sidebarSectionTop">
        <sidebar-nav-item text="Home" icon="icon_home" destination="/" />
        <sidebar-nav-item
          text="Search"
          icon="icon_search"
          destination="/search"
        />
        <sidebar-nav-item
          text="Your Library"
          icon="icon_library"
          destination="/library"
        />
      </div>

      <!-- Create Dashboard, Liked Insights, Your Company -->
      <div class="sidebarSectionPadded">
        <sidebar-nav-item
          text="Create Dashboard"
          icon="icon_add_dashboard"
          destination=""
        />
        <sidebar-nav-item
          text="Liked Insights"
          icon="icon_liked_insights"
          destination=""
        />
        <sidebar-nav-item
          text="Your Company"
          icon="icon_your_company"
          destination="/company/drmartens"
        />
      </div>

      <!-- Separating Bar -->
      <hr class="separatingBar" />
    </div>

    <!-- The bottom, scrollable sidebar content taking up the rest of the space -->
    <sidebar-dashboard-list
      class="sidebarSectionBottom"
      :dashboards="temp_dashboards"
    />
  </div>
</template>

<script>
import SidebarDashboardList from './SidebarDashboardListCmp.vue'
import SidebarNavItem from './SidebarNavItemCmp.vue'
import UtilsSvgCmp from '../utils/UtilsSvgCmp.vue'
export default {
  components: { SidebarNavItem, SidebarDashboardList, UtilsSvgCmp },
  name: 'SidebarFull',
  data() {
    return {
      temp_dashboards: [
        {
          name: 'Some Random Dashboard 1 2 2e  we we we we w2 ee ',
          destination: '/dashboard/test1',
        },
        { name: 'Some Random Dashboard 2', destination: '/dashboard/test2' },
        { name: 'Some Random Dashboard 3', destination: '/dashboard/test3' },
        { name: 'Some Random Dashboard 4', destination: '/dashboard/test4' },
        { name: 'Some Random Dashboard 1', destination: '/dashboard/test5' },
        { name: 'Some Random Dashboard 2', destination: '/dashboard/test7' },
        { name: 'Some Random Dashboard 3', destination: '/dashboard/test7' },
        { name: 'Some Random Dashboard 2', destination: '/dashboard/test7' },
        { name: 'Some Random Dashboard 3', destination: '/dashboard/test7' },
        { name: 'Some Random Dashboard 4', destination: '/dashboard/test7' },
        { name: 'Some Random Dashboard 1', destination: '/dashboard/test7' },
        { name: 'Some Random Dashboard 2', destination: '/dashboard/test7' },
        { name: 'Some Random Dashboard 3', destination: '/dashboard/test7' },
        { name: 'Some Random Dashboard 2', destination: '/dashboard/test7' },
        { name: 'Some Random Dashboard 3', destination: '/dashboard/test7' },
        { name: 'Some Random Dashboard 4', destination: '/dashboard/test7' },
        { name: 'Some Random Dashboard 1', destination: '/dashboard/test7' },
        { name: 'Some Random Dashboard 2', destination: '/dashboard/test7' },
        { name: 'Some Random Dashboard 3', destination: '/dashboard/test7' },
        { name: 'Some Random Dashboard 2', destination: '/dashboard/test' },
        { name: 'Some Random Dashboard 3', destination: '/dashboard/test' },
        { name: 'Some Random Dashboard 4', destination: '/dashboard/test' },
        { name: 'Some Random Dashboard 1', destination: '/dashboard/test' },
        { name: 'Some Random Dashboard 2', destination: '/dashboard/test' },
        { name: 'Some Random Dashboard 3', destination: '/dashboard/test' },
        { name: 'Some Random Dashboard 2', destination: '/dashboard/test' },
        { name: 'Some Random Dashboard 3', destination: '/dashboard/test' },
        { name: 'Some Random Dashboard 4', destination: '/dashboard/test' },
        { name: 'Some Random Dashboard 1', destination: '/dashboard/test' },
        { name: 'Some Random Dashboard 2', destination: '/dashboard/test' },
        { name: 'Some Random Dashboard 3', destination: '/dashboard/test' },
      ],
    }
  },
}
</script>

<style scoped lang="sass">
@import "assets/styles/theme"
@import "assets/styles/mixins"

.sidebar
  width: 241px
  height: 100vh
  overflow: hidden

  display: flex
  flex-flow: column

  color: white
  background: $tiki-purple

.sidebarLogo
  max-height: 38px

.tiki_logo
  fill: white

.sidebarSectionPadded
  padding: 24px 24px 0 24px

.separatingBar
  background-color: rgba(84, 84, 84, 0.75)
  border: none
  height: 1px
  margin: 8px 24px 0 24px
  min-height: 1px

.sidebarSectionBottom
  padding: 0 24px
  height: auto
</style>
