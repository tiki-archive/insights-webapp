<template>
  <div class="wideCardList">
    <div class="wideCardGrid">
      <wide-card-list-item
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
import WideCardListItem from './WideCardListItem.vue'
export default {
  components: { WideCardListItem },
  name: 'HomeFull',
  props: {
    cards: {
      type: Array,
      default: () => {
        return [
          {
            title: 'Your Liked Insights',
            source:
              'https://i.scdn.co/image/ab67656300005f1f563ebb538d297875b10114b7',
          },
          {
            title: 'Lex Fridman Pod but like a really long title',
            description:
              'Podcast ab things that can have quite a few characters past space limit',
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

  grid-template: auto/repeat(auto-fill,minmax(max(320px,23%),1fr))
  // auto/repeat(auto-fill,minmax(max(250px,32%),1fr))
  grid-row-gap: min(2.2vh, 22px)
  grid-column-gap: 24px

  justify-content: space-between
</style>
