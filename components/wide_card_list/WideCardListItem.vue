<template>
  <NuxtLink
    class="themeCard wideCard"
    :to="destination == null ? '' : destination"
  >
    <div class="cardContent">
      <img class="cardImage" :src="source" />

      <div class="cardInfo">
        <h2 class="themeCardTitleText">{{ title }}</h2>
        <p class="themeCardDescText">{{ description }}</p>
      </div>
    </div>
  </NuxtLink>
</template>

<script>
export default {
  props: ['title', 'description', 'source', 'destination'],
}
</script>

<style lang="sass" scoped>
@import "assets/styles/theme/default"

.wideCard
  width: 100%
  height: 80px

.cardContent
  height: 100%
  display: flex

.cardImage
  height: 100%

  border-top-left-radius: $card-border-radius
  border-bottom-left-radius: $card-border-radius

.cardInfo
  margin: auto 0
  padding: 0 $card-content-padding
  overflow: hidden
</style>
