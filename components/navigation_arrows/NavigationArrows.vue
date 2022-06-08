<template>
  <span class="navArrowContainer">
    <button
      :class="'navArrow' + [hasPrevPage() ? ' active' : '']"
      @click="navigateBack"
    >
      <utils-svg-cmp class="arrowIcon" name="icon_back_arrow" />
    </button>
    <button
      :class="'navArrow' + [hasNextPage() ? ' active' : '']"
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
  methods: {
    hasPrevPage() {
      return this.$store.getters['navigation/hasPrevPage']
    },
    hasNextPage() {
      return this.$store.getters['navigation/hasNextPage']
    },
    navigateBack() {
      if (!this.hasPrevPage()) return

      this.$store.commit('navigation/navigateBack')
      this.$router.push(this.$store.getters['navigation/getCurrentPage'])
    },
    navigateForward() {
      if (!this.hasNextPage()) return

      this.$store.commit('navigation/navigateForward')
      this.$router.push(this.$store.getters['navigation/getCurrentPage'])
    },
  },
  mounted() {
    // when browser starts going between pages with arrows
    // we can't know where we should be, so we clear nav
    window.onpopstate = function (event) {
      window.$nuxt.$store.commit('navigation/clearNavigation')
    }
  },
  created() {
    // we need to put the first page into nav history
    this.$store.commit('navigation/visitedPage', this.$route.path)
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
