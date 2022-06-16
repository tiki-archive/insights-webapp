<template>
  <span class="navArrowContainer">
    <button
      :class="'navArrow' + [hasPrevPage ? ' active' : '']"
      @click="navigateBack"
    >
      <utils-svg-cmp class="arrowIcon" name="icon_back_arrow" />
    </button>
    <button
      :class="'navArrow' + [hasNextPage ? ' active' : '']"
      @click="navigateForward"
    >
      <utils-svg-cmp class="arrowIcon" name="icon_forward_arrow" />
    </button>
  </span>
</template>

<script>
import UtilsSvgCmp from '../utils/UtilsSvgCmp.vue'
export default {
  components: { UtilsSvgCmp },
  name: 'NavigationArrows',
  props: [],
  data() {
    return {
      hasPrevPage: false,
      hasNextPage: false,
    }
  },
  methods: {
    navigateBack() {
      if (this.hasPrevPage) history.back()
    },
    navigateForward() {
      if (this.hasNextPage) history.forward()
    },
    // When a page is loaded we determine if it is new or part of page history
    updateHistory() {
      // Get the current page's absolute position in stack
      let currentPosition = history.state.absPos

      if (currentPosition === undefined) {
        // If it doesn't have a position, it is new -> put it on top of stack
        currentPosition = Number(sessionStorage.getItem('lastPosition')) + 1

        sessionStorage.setItem('historyLength', currentPosition)

        // (1) Stamp the entry with its own position in the stack
        history.replaceState({ absPos: currentPosition }, /* no title */ '')
      }

      // (2) Keep track of the last position shown
      sessionStorage.setItem('lastPosition', currentPosition)

      this.hasPrevPage = currentPosition > 1
      this.hasNextPage =
        currentPosition < sessionStorage.getItem('historyLength')
    },
  },
  mounted() {
    this.updateHistory()
  },
  watch: {
    $route() {
      this.updateHistory()
    },
  },
}
</script>

<style scoped lang="sass">
@import "assets/styles/theme"
.navArrowContainer
  display: flex

  gap: 16px

  margin: auto 16px auto 32px
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

  &.active
    &:hover
      background-color: lighten($tiki-purple, 3%)

.arrowIcon
  margin: auto

   // Make svg white when active
  .active > &
    filter: brightness(10)
</style>
