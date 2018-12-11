<template>
  <div class="TopPage">
    <div class="header">
      <h1>投票アプリ</h1>
    </div>
    <div class="contents">
      <h2>ユーザ登録</h2>
      <form @submit.prevent="registration">
        <label>
          <p>ユーザ名</p>
          <input type="text" placeholder="名前を入力して下さい" v-model="InputName" pattern="^[^#\.\$\[\]/]+$">
        </label>
        <button type="submit">問題1に進む</button>
      </form>
    </div>
  </div>
</template>

<script>
import router from '../router'
import firebase from 'firebase'

export default {
  data () {
    return {
      InputName: '',
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

<style scoped>
input[type="text"] {
  margin: 8px auto;
  padding: 5px;
  border: solid 1px lightgray;
  border-radius: 3px;
  outline: none;
  background: none;
  box-shadow: inner 0 0 4px rgba(0, 0, 0, 0.2);
  color: black;
  font-size: 12px;
}

input[type="text"]::placeholder {
  color: lightgray;
  font-size: 12px;
}
</style>
