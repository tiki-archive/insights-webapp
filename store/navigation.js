export const state = () => ({
  pagesVisited: [],
  currentIndex: -1,
})

export const mutations = {
  visitedPage(state, route) {
    // don't stack the same page multiple times in history
    if (state.pagesVisited[state.currentIndex] === route) return

    // remove all forward history if they go down a different path
    if (state.pagesVisited.length > state.currentIndex + 1) {
      state.pagesVisited.splice(
        state.currentIndex + 1,
        state.pagesVisited.length,
        route
      )
    } else {
      state.pagesVisited.push(route)
    }

    state.currentIndex++
  },
  navigateBack(state) {
    state.currentIndex--
  },
  navigateForward(state) {
    state.currentIndex++
  },
  clearNavigation(state) {
    state.currentIndex = -1
    state.pagesVisited = []
  },
}

export const getters = {
  getCurrentPage(state) {
    return state.pagesVisited[state.currentIndex]
  },
  hasPrevPage(state) {
    return state.currentIndex > 0
  },
  hasNextPage(state) {
    return state.pagesVisited.length > state.currentIndex + 1
  },
}
