<template>
  <NuxtLink
    class="themeCard tallCard"
    :to="destination == null ? '' : destination"
  >
    <div class="cardContent">
      <img class="cardImage" :src="source" />

      <div class="cardInfo">
        <h2 class="themeCardTitleText">{{ title }}</h2>
        <p class="themeCardDescText cardDesc">{{ description }}</p>
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
@import "assets/styles/theme"
@import "assets/styles/theme/default"

.tallCard
  width: 100%

.cardContent
  margin: 0 auto
  padding: $card-content-padding

.cardImage
  width: 100%
  margin: 0 auto
  display: block
  border-radius: 4px

.cardInfo
  min-height: 62px

  padding-top: $card-content-padding

.cardDesc
  padding-top: 4px

  display: -webkit-box
  -webkit-box-orient: vertical
  -webkit-line-clamp: 2

  white-space: normal
</style>
