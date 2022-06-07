export const state = () => ({
  pagesVisited: [],
  currentIndex: -1,
})

export const mutations = {
  visitedPage(state, routeName) {
    // remove all forward history if they go down a different path
    if (state.pagesVisited.length > state.currentIndex + 1) {
      state.pagesVisited.splice(
        state.currentIndex,
        state.pagesVisited.length,
        routeName
      )
    } else {
      state.pagesVisited.push(routeName)
    }

    state.currentIndex++
  },

  goNextPage(state, routeName) {
    state.currentIndex++
  },

  goPreviousPage(state, routeName) {
    state.currentIndex--
  },
}
