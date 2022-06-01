<template>
  <div class="insightList">
    <div v-for="(item, index) in insights" :key="index" class="insight">
      <span v-if="number == true" class="ranking"> {{ index + 1 }} </span>
      <insight-list-item
        :name="item.name"
        :icon="item.icon"
        :confidence_level="item.confidence_level2"
      />
    </div>
  </div>
</template>

<script>
import InsightListItem from './InsightListItem.vue'
export default {
  components: { InsightListItem },
  props: {
    number: {
      type: Boolean,
      default: false,
    },
    insights: {
      type: Array,
      default: () => {
        return [
          {
            name: 'Newsletter Performance',
            icon: 'icon_insight_horizontal_bar',
            confidence_level: 95,
          },
          {
            name: 'Customer Ages',
            icon: 'icon_insight_vertical_bar',
            confidence_level: 94,
          },
          {
            name: 'Inbox Profile',
            icon: 'icon_insight_circle',
            confidence_level: 99,
          },
          {
            name: 'Best Subject Lines',
            icon: 'icon_insight_horizontal_bar',
            confidence_level: 98,
          },
          {
            name: 'Customer Locations',
            icon: 'icon_insight_map',
            confidence_level: 95,
          },
        ]
      },
    },
  },
}
</script>

<style scoped lang="sass">
@import "assets/styles/theme"

.insight
  display: flex
  flex-direction: row
  margin: auto 0

  border-radius: 4px

  &:hover
    background: rgba(84, 84, 84, 0.4)

.ranking
  color: $text-gray
  margin: auto 12px auto

.insightList
  display: flex
  flex-direction: column
</style>
