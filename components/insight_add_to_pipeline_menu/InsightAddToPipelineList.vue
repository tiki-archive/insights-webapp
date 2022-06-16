<template>
  <ul class="pipelineListContainer">
    <li v-for="(item, index) in pipelines" :key="index">
      <button class="pipelineButton">
        <span class="buttonIconContainer">
          <img
            class="buttonIcon"
            :src="require(`~/assets/images/png/` + item.icon + `.png`)"
          />
          <!-- <utils-svg-cmp class="buttonIcon" :name="item.icon" /> -->
        </span>
        <span class="themeCardTitleText">{{ item.name }}</span>
        <utils-svg-cmp class="buttonArrow" name="icon_arrow_right" />
      </button>
    </li>
  </ul>
</template>

<script>
export default {
  props: ['pipelines'],
  /*
  Dashboards is a list of objects with a name key/val
  */
}
</script>

<style scoped lang="sass">
@import "assets/styles/theme/default"
@import "assets/styles/mixins"

.pipelineListContainer
  height: 100%
  width: 100%

  padding: 0 16px
  margin: 0

  box-sizing: border-box

  overflow-y: scroll
  overflow-x: hidden

  overflow: overlay

  justify-content: center

  list-style: none
  gap: 10px

  display: flex
  flex-direction: column

li
  margin: 0
  padding: 0
.pipelineButton
  border: 0
  outline: 0
  margin: auto auto
  background: rgba(255, 255, 255, 0.15)

  border-radius: 4px
  padding: 13px 11px 13px 0px

  font-family: $font-family-nunito-sans

  height: 50px
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

  &:hover
    color: white

    transform: scale(1.03)
  > .buttonArrow
    margin-left: auto
    margin-right: 0

.buttonIconContainer
  background-color: rgba(240, 240, 240, .1)
  margin-left: 0
  margin-right: 16px
  height: 50px
  width: 50px

  display: flex
.buttonIcon
  margin: auto auto
</style>
