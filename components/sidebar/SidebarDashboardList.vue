<template>
  <ul class="sidebarNavItemContainer">
    <li v-for="item in dashboards" :key="item.name">
      <NuxtLink class="navItem" :to="item.destination">
        <span class="navText">{{ item.name }}</span>
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

.sidebarNavItemContainer
  margin: auto 0 30px
  padding: 0
  height: 90%

  overflow-y: scroll
  overflow-x: hidden

  list-style: none
  display: block

.navItem
  height: 30px
  display: flex

  text-decoration: none

.navText
  margin: auto 0 0

  font-size: 0.875rem
  line-height: 1rem
  font-weight: 400


  color: $text-gray

  &:hover
    color: white

-webkit-scrollbar
  width: 12px

-webkit-scrollbar-track
  display: hidden

-webkit-scrollbar-thumb
  background-color: rgb(179, 179, 179)
</style>
