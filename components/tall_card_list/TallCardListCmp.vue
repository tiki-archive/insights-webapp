<template>
  <div :class="'tallCardGrid' + (show_all ? '' : ' oneRowGrid')">
    <tall-card-list-item
      v-for="item in cards"
      :key="item.name"
      :title="item.title"
      :description="item.description"
      :source="item.source"
    />
  </div>
</template>

<script>
import TallCardListItem from './TallCardListItemCmp.vue'
export default {
  components: { TallCardListItem },
  name: 'HomeFull',
  props: {
    show_all: {
      type: Boolean,
      default: false,
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
@import "assets/styles/theme/default"
.tallCardGrid
  display: grid

  grid-template: auto/repeat(auto-fill,minmax(max(180px,10%),1fr))

  grid-column-gap: $page-col-gap
  grid-row-gap: $page-row-gap

  justify-content: space-between

.oneRowGrid
  grid-auto-rows: 0
  grid-row-gap: 0
  overflow-y: hidden
</style>
