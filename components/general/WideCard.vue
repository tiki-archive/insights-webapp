<template>
  <div class="wideCard">
    <div class="cardContent">
      <img class="cardImage" :src="source" />

      <div class="cardInfo">
        <h2 class="cardTitle">{{ title }}</h2>
        <p class="cardDesc">{{ description }}</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: ['title', 'description', 'source', 'destination'],
}
</script>

<style lang="sass" scoped>
@import "assets/styles/theme"

.wideCard
  width: 100%
  background: rgba(84, 84, 84, 0.25)
  border-radius: 4px

.cardContent
  margin: 0
  display: flex

.cardImage
  width: 80px
  height: 80px
  margin: 0 0
  display: block
  border-top-left-radius: 4px
  border-bottom-left-radius: 4px

.cardInfo
  margin: auto 0
  padding-left: 16px

.cardTitle
  color: white
  font-size: 1em
  margin: 0

.cardDesc
  color: $text-gray
  font-size: 0.8em
  margin: 0
</style>
