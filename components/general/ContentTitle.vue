<template>
  <h1 class="contentTitle">{{ text }}</h1>
</template>

<script>
export default {
  props: ['text'],
}
</script>

<style lang="sass" scoped>
@import "assets/styles/theme"

.contentTitle
  color: $content-title-color
  font: $font-family-nunito-sans
  font-weight: 800
  font-size: 1.8rem
</style>
