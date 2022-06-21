<template>
  <NuxtLink class="topResultCard" :to="destination == null ? '' : destination">
    <span class="cardContent">
      <img class="cardImage" :src="image" />

      <span class="cardInfo">
        <h2 class="cardTitle">{{ title }}</h2>
        <span class="cardDesc">
          <span class="cardAuthor">By {{ author }}</span>
          <span :class="'cardType ' + result_type.toLowerCase()">{{
            result_type
          }}</span>
        </span>
      </span>
    </span>
  </NuxtLink>
</template>

<script>
export default {
  props: ['title', 'author', 'result_type', 'image', 'destination'],
}
</script>

<style lang="sass" scoped>
@import "assets/styles/theme"

.topResultCard
  width: 100%
  height: 100%
  max-height: 100%

  background: rgba(84, 84, 84, 0.25)
  border-radius: 8px

  display: block

  text-decoration: none

  &:hover
    background: rgba(84, 84, 84, 0.4)

.cardContent
  width: 100%
  height: 100%

  box-sizing: border-box
  padding: 30px 30px 18px 30px

  display: flex
  flex-direction: column
  justify-content: flex-end

.cardImage
  width: 108px

  margin: auto auto auto 0

  display: block

  border-radius: 14px

.cardInfo
  min-height: calc(20px + 3.5rem)
  overflow: hidden

.cardTitle
  color: white

  font-size: calc(.875rem + 130%)
  font-weight: 700

  padding-top: 16px
  margin: 0

  white-space: nowrap
  overflow: hidden
  text-overflow: ellipsis

.cardDesc
  color: $text-gray

  font-size: 0.875rem
  line-height: 1rem

  padding: 5px

  display: flex

.cardAuthor
  margin: auto 0px

.cardType
  background-color: darkblue
  color: white
  margin: auto 18px
  padding: 4px 12px
  border-radius: 14px

.dashboard
  background-color: $tiki-purple

.company
  background-color: darkgreen

.insight
  background-color: darkred
</style>
