<template>
  <div class="ShowScore">
    <div class="header">
      <h1>投票アプリ</h1>
    </div>
    <div class="contents">
      <h2>スコア</h2>
      <button v-on:click="show">表示</button>
      <table align="center">
        <tr>
          <th>順位</th>
          <th>名前</th>
          <th>ポイント</th>
        </tr>
        <tr v-for="(value, key) in scores" :key="key">
          <td>{{ key + 1 }} 位</td>
          <td>{{ value.username }}</td>
          <td>{{ value.point }}</td>
        </tr>
      </table>
    </div>
  </div>
</template>

<script>
import firebase from 'firebase'

export default {
  data () {
    return {
      bounen: [],
      bounenRef: null,
      database: null,
      scores: []
    }
  },
  methods: {
    show: async function (e) {
      var scores = []
      this.database = firebase.database()
      this.bounenRef = this.database.ref('bounen')

      await this.bounenRef.once('value', function (snapshot) {
        snapshot.forEach(player => {
          let score = 0
          player.forEach(q => {
            switch (q.key) {
              case 'Q1':
                score += calcQ1(q.val())
                break
              case 'Q2':
                score += calcQ2(q.val())
                break
              case 'Q3':
                score += calcQ3(q.val())
                break
              case 'Q4':
                score += calcQ4(q.val())
                break
              case 'Q5':
                score += calcQ5(q.val())
                break
              case 'Q6':
                score += calcQ6(q.val())
                break
            }
          })
          scores.push({username: player.key, point: score})
        })
      })

      await scores.sort(function (a, b) {
        return a.point > b.point ? -1 : 1
      })
      this.scores = scores
    }
  }
}

function calcQ1 (arr) {
  // winner: 1
  var score = arr[1] * 2 - (arr[2] + arr[3])
  return score
}

function calcQ2 (arr) {
  // winner: 2
  var score = arr[2] * 2 - (arr[1] + arr[3])
  return score
}

function calcQ3 (arr) {
  // winner: 3
  var score = arr[3] * 2 - (arr[1] + arr[2])
  return score
}

function calcQ4 (arr) {
  // winner: 2
  var score = arr[2] * 3 - (arr[1] + arr[3] + arr[4])
  return score
}

function calcQ5 (arr) {
  // winner: 1
  var score = arr[1] * 3 - (arr[2] + arr[3] + arr[4])
  return score
}

function calcQ6 (arr) {
  // winner: 3
  var score = arr[3] * 3 - (arr[1] + arr[2] + arr[4])
  return score
}

</script>

<style scoped>
button {
  margin-bottom: 4px;
}

th:nth-child(1), td:nth-child(1) {
  width: 64px;
}

th:nth-child(3), td:nth-child(3) {
  width: 96px;
}
</style>
