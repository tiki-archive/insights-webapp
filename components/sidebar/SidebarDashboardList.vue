<template>
  <ul class="sidebarNavItemContainer">
    <li v-for="item in dashboards" :key="item.name">
      <NuxtLink
        :class="[
          $nuxt.$route.path == item.destination
            ? 'navLink currentlySelected'
            : 'navLink',
        ]"
        :to="item.destination"
      >
        {{ item.name }}
      </NuxtLink>
    </li>
  </ul>
</template>

<script>
export default {
  props: ['dashboards'],
  /*
  Dashboards is a list of objects with a name and destination
  */
}
</script>

<style scoped lang="sass">
@import "assets/styles/theme"
@import "assets/styles/mixins"

.sidebarNavItemContainer
  margin: auto 0 30px
  padding: 0

  overflow-y: scroll
  overflow-x: hidden

  list-style: none

  display: flex
  flex-direction: column

.navLink
  text-decoration: none

  height: 30px
  display: flex
  align-items: flex-end

  white-space: nowrap
  overflow: hidden

  font-size: 0.875rem
  line-height: 1rem
  font-weight: 400

  color: $text-gray

  &:hover, &.currentlySelected
    color: white
</style>
