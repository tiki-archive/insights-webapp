<template>
  <div class="themeStandardPageContainer">
    <!-- <search-bar /> -->

    <span v-if="searchTerm">
      <section class="themeMultiContentSection topSection">
        <span class="topResult">
          <h2 class="titleText">Top results for {{ searchTerm }}</h2>

          <top-result-card
            title="Top Selling Products"
            image="https://aux.iconspalace.com/uploads/amazon-icon-256.png"
            author="TIKI"
            result_type="Dashboard"
            class="topResultCard"
          />
        </span>

        <span class="secondaryResult">
          <content-heading text="Insights" link="/search/insights/test" />

          <insight-list />
        </span>
      </section>

      <section>
        <content-heading text="Dashboards" link="/search/dashboards/test" />

        <tall-card-list
          :cards="[
            {
              title: 'Top Fashion Brands',
              description: 'Email analytics, sales numbers, and more!',
              source:
                'https://cdn3.iconfinder.com/data/icons/clothing-set-4/64/tshirt-other-512.png',
            },
            {
              title: 'Mobile Gaming Email',
              description:
                'Player retention, micro transaction data, and more!',
              source:
                'https://upload.wikimedia.org/wikipedia/en/9/90/Jetpack_Joyride_iOS.png',
            },
            {
              title: 'Drop Shipping',
              description: 'Top products, email data, and more!',
              source:
                'https://blog.placeit.net/wp-content/uploads/2018/06/dropshipping-icon-v4.png',
            },
          ]"
        />
      </section>

      <section>
        <content-heading text="Companies" link="/search/companies/test" />

        <tall-card-list
          :cards="[
            {
              title: 'SendGrid',
              source:
                'https://pbs.twimg.com/profile_images/1153335496795414530/Af2RRy1K_400x400.jpg',
            },
          ]"
        />
      </section>
    </span>

    <span v-else>
      <section>
        <content-heading
          text="Recent searches"
          link="/search/dashboards/test"
        />

        <tall-card-list
          :cards="[
            {
              title: 'Nike',
              description: 'Top selling shoes',
              source: 'https://thumbs.dreamstime.com/b/web-183282388.jpg',
            },
            {
              title: 'Marvel',
              description: 'Top films',
              source:
                'https://1.bp.blogspot.com/-aHEAfsR3ryI/X3Z8bwh28VI/AAAAAAAAC5k/Gkhm8jWvRnAcr67Ls8Blxm4xFpHvn8yCwCLcBGAsYHQ/s400/Client-Square-Marvel-Studios.png',
            },
            {
              title: 'Pacsun',
              description: 'Top selling shirts',
              source: 'https://assets.simon.com/tenantlogos/4402.png',
            },
          ]"
        />
      </section>
    </span>
  </div>
</template>

<script>
import TopResultCard from '~/components/top_result_card/TopResultCardCmp.vue'
import InsightList from '~/components/insight_list/InsightListCmp.vue'
import ContentHeading from '~/components/content_heading/ContentHeadingCmp.vue'
import TallCardList from '~/components/tall_card_list/TallCardListCmp.vue'

export default {
  name: 'HomeFull',
  components: {
    TopResultCard,
    InsightList,
    ContentHeading,
    TallCardList,
  },
  data() {
    return {
      searchTerm: this.$route.params.search,
    }
  },
  created() {
    this.$nuxt.$on('searchTermChanged', (newTerm) => {
      this.searchTerm = newTerm
    })
  },
  scrollToTop: true,
}
</script>

<style scoped lang="sass">
@import "assets/styles/theme/default"
.topResultCard
  height: 260px
  width: 30vw

  box-sizing: border-box
.secondaryResult
  min-width: 400px
  width: calc(100% - 30vw - $page-col-gap)
  box-sizing: border-box
</style>
