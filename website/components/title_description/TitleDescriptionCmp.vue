<template>
  <div class="titleDescription">
    <h3>{{ title }}</h3>
    <span class="descriptionText">{{ description }}</span>
  </div>
</template>

<script>
export default {
  props: ['title', 'description'],
}
</script>

<style lang="sass" scoped>
@import "assets/styles/theme"

h3
  margin: 0 0 4px

.descriptionText
  color: $text-gray
</style>
