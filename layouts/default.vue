<template>
  <Nuxt />
</template>

<script>
export default {
  name: 'DefaultLayout',
}
</script>

<style lang="sass">
@import "assets/styles/theme"

body
  margin: 0
  font-family: $font-family-nunito-sans

::-webkit-scrollbar
  width: 12px

::-webkit-scrollbar-track
  display: hidden

::-webkit-scrollbar-thumb
  background-color: rgb(179, 179, 179)
</style>
