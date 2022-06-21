<template>
  <div class="loginContainer">
    <span class="form">
      <img
        src="https://gyazo.com/b60691ad912acae6d882cc014db7f00d.png"
        width="100%"
      />
    </span>

    <nuxt-link class="purpleButton" to="/home">
      <span>Log In</span>
    </nuxt-link>

    <span class="otherAction">
      Don't have an account?
      <nuxt-link class="otherActionLink" to="/register">Sign up</nuxt-link>.
    </span>
  </div>
</template>

<script>
export default {
  name: 'RegisterPage',
  layout: 'form',
  scrollToTop: true,
}
</script>

<style scoped lang="sass">
@import "assets/styles/theme"

.loginContainer
  display: flex
  flex-direction: column

  margin: auto auto

.otherAction
  font-size: 1rem

  font-weight: 400
  letter-spacing: 0px

  text-align: center

.otherActionLink
  color: $tiki-purple
  text-decoration: underline

  &:hover
    color: $tiki-pink
</style>
