<template>
  <div class="navbar" id="navbar">
    <navigation-arrows />

    <search-bar v-if="showSearch == true" />

    <profile-button
      v-if="this.loggedIn"
      class="userInfo"
      :name="name"
      :icon="icon"
    />

    <span v-else class="accountActions">
      <nuxt-link class="signupButton" to="/register">
        <span>Sign up</span>
      </nuxt-link>

      <nuxt-link class="loginButton" to="/login">
        <span>Login</span>
      </nuxt-link>
    </span>
  </div>
</template>

<script>
import ProfileButton from '../profile_button/ProfileButton.vue'
import SearchBar from '../search_bar/SearchBar.vue'
export default {
  components: { ProfileButton, SearchBar },
  name: 'SidebarFull',
  props: ['name', 'icon', 'showSearch'],
  data() {
    return {
      loggedIn: false,
    }
  },
  methods: {
    onScroll(event) {
      if (event.target.className.startsWith('mainContainer')) {
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
  width: calc(100vw - 241px)
.userInfo
  margin: auto 32px auto auto
  float: right

.accountActions
  margin: auto 32px auto auto
  display: flex
  gap: 32px

.signupButton
    margin: auto
    padding: 0

    color: $gray-1
    font-weight: 700
    text-decoration: none

    transition: all .1s ease-in-out

    &:hover
        transform: scale(1.03)
        color: white
.loginButton
    margin: auto
    padding: 12px 32px
    border-radius: 500px

    background-color: white
    color: $tiki-purple
    text-decoration: none

    font-weight: 700

    transition: all .1s ease-in-out

    &:hover
        transform: scale(1.03)
        background-color: $gray-1
</style>
