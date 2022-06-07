<template>
  <div class="plainPage">
    <Nuxt id="nuxt" />
  </div>
</template>

<script>
export default {
  name: 'PlainLayout',
}
</script>

<style lang="sass">
@import "assets/styles/theme"
@import "assets/styles/mixins"

body
  margin: 0
  font-family: $font-family-nunito-sans

  overflow: visible

.plainPage
  width: 100%

  overflow-x: hidden
  overflow-y: scroll

  display: flex

  margin: auto auto
</style>
