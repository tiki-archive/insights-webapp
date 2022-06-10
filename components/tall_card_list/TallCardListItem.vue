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

  text-decoration: none

  &:hover
    background: rgba(84, 84, 84, 0.4)

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
  min-height: calc(20px + 3.5rem)
  overflow: hidden

.cardTitle
  color: white

  font-size: 1rem
  line-height: 1.5rem

  padding-top: 16px
  margin: 0

  white-space: nowrap
  overflow: hidden
  text-overflow: ellipsis

.cardDesc
  color: $text-gray

  font-size: 0.875rem
  line-height: 1rem

  padding-top: 4px
  margin: 0

  display: -webkit-box
  -webkit-box-orient: vertical
  -webkit-line-clamp: 2
  text-overflow: ellipsis
</style>
