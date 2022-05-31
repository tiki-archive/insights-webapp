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
        <sidebar-nav-item
          text="Home"
          icon="icon_home"
          destination=""
          selected="true"
        />
        <sidebar-nav-item
          text="Search"
          icon="icon_search"
          destination="search"
        />
        <sidebar-nav-item
          text="Your Library"
          icon="icon_library"
          destination="library"
        />
      </div>

      <!-- Create Dashboard, Liked Insights, Your Company -->
      <div class="sidebarSectionPadded">
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
    <sidebar-dashboard-list
      class="sidebarSectionBottom"
      :dashboards="temp_dashboards"
    />
  </div>
</template>

<script>
import SidebarDashboardList from './SidebarDashboardList.vue'
import SidebarNavItem from './SidebarNavItem.vue'
import UtilsSvgCmp from '../utils/UtilsSvgCmp.vue'
export default {
  components: { SidebarNavItem, SidebarDashboardList, UtilsSvgCmp },
  name: 'SidebarFull',
  data() {
    return {
      temp_dashboards: [
        {
          name: 'Some Random Dashboard 1 2 2e  we we we we w2 ee ',
          destination: 'to',
        },
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
@import "assets/styles/mixins"

.sidebar
  width: 243px
  height: 100vh
  overflow: hidden

  display: flex
  flex-flow: column

  color: white
  background: $tiki-purple

.sidebarLogo
  max-height: 38px

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

@include for-phone
  .sidebar
    width: 100%
    height: 90vh
    overflow: hidden

  .sidebarLogoContainer
    display: none

  .sidebarSectionTop
    padding-top: 0
</style>
