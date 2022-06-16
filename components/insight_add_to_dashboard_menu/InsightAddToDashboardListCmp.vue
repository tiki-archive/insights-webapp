<template>
  <ul class="dashboardListContainer">
    <li v-for="(item, index) in dashboards" :key="index">
      <button class="dashboardButton">
        <span class="themeCardTitleText">{{ item.name }}</span>
        <utils-svg-cmp name="icon_arrow_right" />
      </button>
    </li>
  </ul>
</template>

<script>
export default {
  props: ['dashboards'],
  /*
  Dashboards is a list of objects with a name key/val
  */
}
</script>

<style scoped lang="sass">
@import "assets/styles/theme/default"
@import "assets/styles/mixins"

.dashboardListContainer
  height: 100%
  width: 100%

  padding: 0 16px
  margin: 0

  box-sizing: border-box

  overflow-y: scroll
  overflow-x: hidden

  overflow: overlay

  justify-content: flex-start

  list-style: none
  gap: 10px

  display: flex
  flex-direction: column

li
  margin: 0
  padding: 0
.dashboardButton
  border: 0
  outline: 0
  margin: auto auto
  background: rgba(255, 255, 255, 0.15)


  border-radius: 4px
  padding: 13px 11px 13px 19px

  font-family: $font-family-nunito-sans

  height: 52px
  width: 100%
  max-width: 325px

  font-size: 1rem
  line-height: 1.5rem

  display: flex

  white-space: nowrap
  overflow: hidden

  color: white
  align-items: center

  cursor: pointer

  &:hover, &.currentlySelected
    color: white

    transform: scale(1.03)

  > svg
    margin-left: auto
    margin-right: 0
</style>
