<template>
  <div class="navbar" id="navbar">
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

    <search-bar v-if="showSearch == true" />

    <router-link to="/">
      <span style="color: white">{{ this.$store.state.navigation }}</span>
    </router-link>

    <profile-button class="userButton" :name="name" :icon="icon" />
  </div>
</template>

<script>
import UtilsSvgCmp from '../utils/UtilsSvgCmp.vue'
import ProfileButton from '../profile_button/ProfileButton.vue'
import SearchBar from '../search_bar/SearchBar.vue'
export default {
  components: { UtilsSvgCmp, ProfileButton, SearchBar },
  name: 'SidebarFull',
  props: ['name', 'icon', 'showSearch'],
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
    hasPrevPage() {
      return this.$store.getters['navigation/hasPrevPage']
    },
    hasNextPage() {
      return this.$store.getters['navigation/hasNextPage']
    },
    navigateBack() {
      if (!this.hasPrevPage()) return

      this.$store.commit('navigation/navigateBack', this.to)
      this.$router.push(this.$store.getters['navigation/getCurrentPage'])
    },
    navigateForward() {
      if (!this.hasNextPage()) return

      this.$store.commit('navigation/navigateForward', this.to)
      this.$router.push(this.$store.getters['navigation/getCurrentPage'])
    },
  },
  mounted() {
    window.addEventListener('scroll', this.onScroll, true)
  },
  beforeDestroy() {
    window.removeEventListener('scroll', this.onScroll, true)
  },
  data() {
    return {
      path: '/',
    }
  },
}
</script>

<style scoped lang="sass">
@import "assets/styles/theme"

.navbar
  display: flex
  height: $navbar-height
  position: fixed
  right: 0
  width: calc(100vw - 243px)
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

.userButton
  margin: auto 32px auto auto
  float: right
</style>
