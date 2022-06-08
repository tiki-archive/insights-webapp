<template>
  <div class="navbar" id="navbar">
    <navigation-arrows />

    <search-bar v-if="showSearch == true" />

    <profile-button class="userButton" :name="name" :icon="icon" />
  </div>
</template>

<script>
import ProfileButton from '../profile_button/ProfileButton.vue'
import SearchBar from '../search_bar/SearchBar.vue'
export default {
  components: { ProfileButton, SearchBar },
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
  height: $navbar-height
  position: fixed
  right: 0
  width: calc(100vw - 243px)
.userButton
  margin: auto 32px auto auto
  float: right
</style>
