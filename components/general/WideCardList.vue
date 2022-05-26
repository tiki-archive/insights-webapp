<template>
  <div class="wideCardList">
    <content-title :text="title" />

    <div class="wideCardGrid">
      <wide-card
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
import WideCard from './WideCard.vue'
export default {
  components: { WideCard, ContentTitle },
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
        ]
      },
    },
  },
}
</script>

<style scoped lang="sass">
@import "assets/styles/theme"

.wideCardGrid
  display: grid

  grid-template: auto/repeat(auto-fill,minmax(max(250px,32%),1fr))
  grid-row-gap: min(2.2vh, 22px)
  grid-column-gap: 24px

  justify-content: space-between
</style>
