<template>
  <span class="heading">
    <h2>
      <NuxtLink class="headingLink" :to="link"> {{ text }} </NuxtLink>
    </h2>

    <NuxtLink class="themeSeeAllText" :to="link"> SEE ALL </NuxtLink>
  </span>
</template>

<script>
export default {
  props: ['text', 'link'],
}
</script>

<style scoped lang="sass">
@import "assets/styles/theme/default"
.heading
  display: flex

.headingLink
  color: white
  text-decoration: none

  &:hover
    text-decoration: underline
</style>
