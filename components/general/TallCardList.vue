<template>
  <div class="tallCardList">
    <content-title class="contentTitle" :text="title" />

    <div class="tallCardGrid">
      <tall-card
        v-for="item in cards"
        :key="item.name"
        :title="item.title"
        :description="item.description"
        :source="item.source"
        class="card"
      />
    </div>
  </div>
</template>

<script>
import ContentTitle from './ContentTitle.vue'
import TallCard from './TallCard.vue'
export default {
  components: { TallCard, ContentTitle },
  name: 'HomeFull',
  props: {
    title: {
      type: String,
    },
    cards: {
      type: Array,
      default: () => {
        return [
          {
            title: 'Lex Fridman Pod',
            description: 'Podcast ab things',
            source:
              'https://i.scdn.co/image/ab67656300005f1f563ebb538d297875b10114b7',
          },
          {
            title: 'Lex Fridman Pod',
            description: 'Podcast ab things',
            source:
              'https://i.scdn.co/image/ab67656300005f1f563ebb538d297875b10114b7',
          },
          {
            title: 'Lex Fridman Pod',
            description: 'Podcast ab things',
            source:
              'https://i.scdn.co/image/ab67656300005f1f563ebb538d297875b10114b7',
          },
          {
            title: 'Lex Fridman Pod',
            description: 'Podcast ab things',
            source:
              'https://i.scdn.co/image/ab67656300005f1f563ebb538d297875b10114b7',
          },
          {
            title: 'Lex Fridman Pod',
            description: 'Podcast ab things',
            source:
              'https://i.scdn.co/image/ab67656300005f1f563ebb538d297875b10114b7',
          },
          {
            title: 'Lex Fridman Pod',
            description: 'Podcast ab things',
            source:
              'https://i.scdn.co/image/ab67656300005f1f563ebb538d297875b10114b7',
          },
          {
            title: 'Lex Fridman Pod',
            description: 'Podcast ab things',
            source:
              'https://i.scdn.co/image/ab67656300005f1f563ebb538d297875b10114b7',
          },
          {
            title: 'Lex Fridman Pod',
            description: 'Podcast ab things',
            source:
              'https://i.scdn.co/image/ab67656300005f1f563ebb538d297875b10114b7',
          },
          {
            title: 'Lex Fridman Pod',
            description: 'Podcast ab things',
            source:
              'https://i.scdn.co/image/ab67656300005f1f563ebb538d297875b10114b7',
          },
        ]
      },
    },
  },
}
</script>

<style scoped lang="sass">
@import "assets/styles/theme"

.tallCardGrid
  display: grid

  grid-template: auto/repeat(auto-fill,minmax(max(180px,10%),1fr))
  grid-column-gap: 18px
  grid-row-gap: min(2.2vh, 22px)

  justify-content: space-between
</style>
