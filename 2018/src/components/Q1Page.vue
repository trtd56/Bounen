<template>
  <div class="QPage">
    <div class="header">
      <h1>投票アプリ</h1>
      <p>ユーザ名：{{$route.params.username}}</p>
    </div>
    <div class="contents">
      <h2>問題1 ボール投げ</h2>
      <p>誰に賭ける？</p>
      <table align="center">
      <tr>
      <td width="70">{{player1}}</td>
      <td width="120"><el-slider v-model="value1"></el-slider></td>
      <td width="45">{{ value1 }}</td>
      </tr>
      <tr>
      <td width="70">{{player2}}</td>
      <td width="120"><el-slider v-model="value2"></el-slider></td>
      <td width="45">{{value2}}</td>
      </tr>
      <tr>
      <td width="70">{{player3}}</td>
      <td width="120"><el-slider v-model="value3"></el-slider></td>
      <td width="45">{{value3}}</td>
      </tr>
      </table>
      <button v-on:click="check">回答して次の問題に進む</button>
    </div>
  </div>
</template>

<script>
import router from '../router'
import firebase from 'firebase'

export default {
  name: 'QPage',
  data () {
    return {
      value1: 0,
      value2: 0,
      value3: 0,
      player1: '1) ああ',
      player2: '2) いい',
      player3: '3) うう'
    }
  },
  methods: {
    check: function (event) {
      var res = confirm(
        this.player1 + ': ' + this.value1 + ' ポイント\n' +
        this.player2 + ': ' + this.value2 + ' ポイント\n' +
        this.player3 + ': ' + this.value3 + ' ポイント\n' +
        'よいですか？'
      )
      if (res === true) {
        this.database = firebase.database()
        this.bounenRef = this.database.ref('bounen/' + this.$route.params.username)
        this.bounenRef.update({
          Q1: {
            1: this.value1,
            2: this.value2,
            3: this.value3
          }
        })
        router.push({name: 'Q2Page', params: {username: this.$route.params.username}})
      }
    }
  }
}
</script>

<style>
</style>
