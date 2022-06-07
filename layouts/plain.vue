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

.plainPage
  width: 100%

  overflow-x: hidden
  overflow-y: scroll

  display: flex

  margin: auto auto
</style>
