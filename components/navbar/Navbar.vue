<template>
  <div class="navbar" id="navbar">
    <span class="navArrowContainer">
      <button
        :class="
          'navArrow' +
          [1 == 0 /* TODO: IMPLEMENT BACK ARROW */ ? ' active' : '']
        "
      >
        <utils-svg-cmp class="arrowIcon" name="icon_back_arrow" />
      </button>
      <button
        :class="
          'navArrow' +
          [1 == 1 /* TODO: IMPLEMENT FORWARD ARROW */ ? ' active' : '']
        "
      >
        <utils-svg-cmp class="arrowIcon" name="icon_forward_arrow" />
      </button>
    </span>

    <button class="userButton">
      <img class="userIcon" :src="icon" />
      <span class="userName">{{ name }}</span>
      <utils-svg-cmp class="downArrow" name="icon_down_arrow" />
    </button>
  </div>
</template>

<script>
import UtilsSvgCmp from '../utils/UtilsSvgCmp.vue'
export default {
  components: { UtilsSvgCmp },
  name: 'SidebarFull',
  props: ['name', 'icon'],
  methods: {
    onScroll(event) {
      if (event.target.className === 'mainContainer') {
        this.pos = event.target.scrollTop
        if (event.target.scrollTop < 64) {
          const opa = event.target.scrollTop / 64.0
          document.getElementById('navbar').style.backgroundColor =
            'rgb(64, 44, 67, ' + opa + ')'
        } else {
          document.getElementById('navbar').style.backgroundColor =
            'rgb(64, 44, 67)'
        }
      }
    },
  },
  mounted() {
    window.addEventListener('scroll', this.onScroll, true)
  },
  beforeDestroy() {
    window.removeEventListener('scroll', this.onScroll, true)
  },
}
</script>

<style scoped lang="sass">
@import "assets/styles/theme"

.navbar
  display: flex
  height: 64px
  position: fixed
  right: 0
  width: calc(100vw - 243px)

.navArrowContainer
  display: flex

  gap: 16px

  margin: auto 32px
  float: left

.navArrow
  display: flex
  align-items: center

  border: 0

  height: 32px
  width: 32px
  border-radius: 4100%

  padding: 2px

  background-color: $tiki-purple

  &:hover
    background-color: lighten($tiki-purple, 3%)

.arrowIcon
  margin: auto

   // Make svg white when active
  .active > &
    filter: brightness(10)


.userButton
  display: flex
  align-items: center

  border: 0
  border-radius: 23px
  background-color: $tiki-purple

  gap: 8px
  padding: 2px
  height: 32px

  margin: auto 32px auto auto

  float: right


  &:hover
    background-color: lighten($tiki-purple, 3%)

.userIcon
  width: 28px
  height: 28px
  display: inline-block

  border-radius: 23px

.userName
  color: white
  font-family: $font-family-nunito-sans
  font-size: .875rem
  font-weight: 700

.downArrow
  margin-right: 8px
</style>
