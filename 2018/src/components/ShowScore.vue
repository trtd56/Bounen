<template>
  <div class="ShowScore">
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
    show: function (event) {
      var scores = []
      this.database = firebase.database()
      this.bounenRef = this.database.ref('bounen')

      this.bounenRef.once('value', function (snapshot) {
        const rootList = snapshot.val()
        // データオブジェクトを配列に変更する
        Object.keys(rootList).forEach((val, _num) => {
          var score = 0
          Object.keys(rootList[val]).forEach((q, point) => {
            if (q === 'Q1') {
              score += calcQ1(rootList[val][q])
            } else if (q === 'Q2') {
              score += calcQ2(rootList[val][q])
            }
          })
          var tmp = {username: val, point: score}
          scores.push(tmp)
        })
      })
      scores.sort(function (a, b) {
        return a.point > b.point ? -1 : 1
      })
      this.scores = scores
    }
  }
}

function calcQ1 (arr) {
  var score = arr[1] * 2 - arr[2] - arr[3]
  return score
}

function calcQ2 (arr) {
  var score = -arr[1] + arr[2] * 2 - arr[3]
  return score
}
</script>

<style>
h2 {
  font-weight: normal;
}
a {
  color: #42b983;
}
.TopPage {
  margin-top: 20px;

  display: flex;
  flex-flow: column nowrap;
  justify-content: center;
  align-items: center
}
input {
  margin: 10px 0;
  padding: 10px;
}

table {
  border: 2px solid #42b983;
  border-radius: 3px;
  background-color: #fff;
}

th {
  background-color: #42b983;
  color: rgba(255,255,255,0.66);
  cursor: pointer;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}

td {
  background-color: #f9f9f9;
}

th, td {
  min-width: 120px;
  padding: 10px 20px;
}
</style>
