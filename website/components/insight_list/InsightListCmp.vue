<template>
  <div class="insightList">
    <div v-for="(item, index) in insights" :key="index" class="insight">
      <span v-if="number == true" class="ranking"> {{ index + 1 }} </span>
      <insight-list-item
        :name="item.name"
        :description="item.description"
        :icon="item.icon"
        :confidence_level="confidence_levels ? item.confidence_level : null"
        :destination="'/insight/top-subject-lines'"
      />
    </div>
  </div>
</template>

<script>
import InsightListItem from './InsightListItemCmp.vue'
export default {
  components: { InsightListItem },
  props: {
    number: {
      type: Boolean,
      default: true,
    },
    confidence_levels: {
      type: Boolean,
      default: true,
    },
    insights: {
      type: Array,
      default: () => {
        return [
          {
            name: 'Top Subject Lines',
            description: 'Amazon',
            icon: 'icon_insight_circle',
            confidence_level: 95,
          },
          {
            name: 'Customer Ages',
            description: 'Google',
            icon: 'icon_insight_vertical_bar',
            confidence_level: 94,
          },
          {
            name: 'Inbox Profile',
            description: 'Global Boot Market',
            icon: 'icon_insight_horizontal_bar',
            confidence_level: 99,
          },
          {
            name: 'Email Performance',
            description: 'Consumer Fashion',
            icon: 'icon_insight_vertical_bar',
            confidence_level: 98,
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
  min-width: 400px
</style>
