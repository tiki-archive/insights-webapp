<template>
  <div class="registerContainer">
    <h1>Sign up to start browsing insights!</h1>

    <span class="form">
      <img
        src="https://gyazo.com/82487a3e83560decaae81b9fb0daf2d3.png"
        width="100%"
      />
    </span>

    <nuxt-link class="purpleButton" to="/home">
      <span>Sign Up</span>
    </nuxt-link>

    <span class="otherAction">
      Have an account?
      <nuxt-link class="otherActionLink" to="/login">Log in</nuxt-link>.
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

h1
  margin: auto

  color: black

  font-size: 1.8rem
  font-weight: 800

  letter-spacing: -0.04em

.registerContainer
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
