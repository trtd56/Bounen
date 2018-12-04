<template>
  <div class="TopPage">
    <img src="../assets/logo.png">
    <h2>投票アプリ</h2>
    <input type="text" placeholder="名前を入力して下さい" v-model="InputName">
    <button v-on:click="registration">問題1に進む</button>
  </div>
</template>

<script>
import router from '../router'
import firebase from 'firebase'

export default {
  data () {
    return {
      InputName: 'test',
      bounen: [],
      bounenRef: null,
      database: null
    }
  },
  methods: {
    registration: function (event) {
      this.database = firebase.database()
      this.bounenRef = this.database.ref('bounen/' + this.InputName)
      this.bounenRef.set({
        Q1: {1: 0, 2: 0, 3: 0},
        Q2: {1: 0, 2: 0, 3: 0}
      })
      router.push({name: 'Q1Page', params: {username: this.InputName}})
    }
  }
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
</style>
