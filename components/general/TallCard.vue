<template>
  <NuxtLink class="tallCard" :to="destination == null ? '' : destination">
    <div class="cardContent">
      <img class="cardImage" :src="source" />

      <div class="cardInfo">
        <h2 class="cardTitle">{{ title }}</h2>
        <p class="cardDesc">{{ description }}</p>
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

.tallCard
  width: 100%
  background: rgba(84, 84, 84, 0.25)
  border-radius: 4px

.cardContent
  width: 84%
  margin: 0 auto
  padding: 7%

.cardImage
  width: 100%
  margin: 0 auto
  display: block
  border-radius: 4px

.cardInfo
  min-height: 62px

.cardTitle
  color: white
  font-size: 1.1em
  padding-top: 16px
  margin: 0

.cardDesc
  color: $text-gray
  font-size: 0.8em
  padding-top: 5px
  margin: 0
</style>
