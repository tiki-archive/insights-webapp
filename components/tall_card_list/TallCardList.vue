<template>
  <div class="tallCardList">
    <div class="tallCardGrid">
      <tall-card-list-item
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
import TallCardListItem from './TallCardListItem.vue'
export default {
  components: { TallCardListItem },
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
            title: 'Liked Insights',
            source:
              'https://i.scdn.co/image/ab67656300005f1f563ebb538d297875b10114b7',
          },
          {
            title: 'Lex Fridman Podcast long',
            description:
              'A two line description is needed if we want to properly describe some insights',
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
